"""Detect which REST API version a Veeam Backup for Microsoft 365 server offers.

The REST API has no endpoint that reports the set of versions a server supports, and
nothing negotiates it for the caller — the version is part of every path, so a client picks
one up front and lives with it.

That path is what makes detection possible without credentials. ``/v8/ServiceInstance``
exists in v6, v7 and v8 alike (see the shipped OpenAPI schemas), and it requires a bearer
token, so an anonymous probe distinguishes the two cases cleanly:

* the server serves that version — routing matches and authentication rejects it: 401
  (or 403, or 200 on a deployment that does not gate it)
* the server does not serve that version — routing finds nothing: 404

``detect_api_version`` intersects the versions that answer with the versions this package
can actually speak (``VERSION_TO_PACKAGE``) and returns the newest, so the answer is always
something the caller can pass straight to ``VeeamClient``.

Detection is best-effort by contract. A server can be unreachable, behind a proxy that
rewrites statuses, or reject the probe for a reason of its own, and all of those return None
so a caller falls back to a version of its own choosing rather than failing outright.

Callers should resolve once and store the result. Re-detecting on every start would silently
move an existing deployment onto a newer version, and versions rename enum values and add
required fields.
"""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Iterable, Sequence
from typing import NamedTuple

import httpx

from .versions import VERSION_TO_PACKAGE

_LOGGER = logging.getLogger(__name__)

# Probes run concurrently, so this bounds the whole detection rather than each version
DEFAULT_TIMEOUT = 8.0

# Requires a bearer token and exists in every version this package ships, so an anonymous
# request separates "this version is served" from "this version is not" by status alone
PROBE_PATH = "/{version}/ServiceInstance"

# Statuses that mean the route exists. 401 is the expected answer to an unauthenticated
# probe; 200 and 403 also prove the path is routed, which is the only question being asked.
# Anything else — 404 above all — means this version is not served here.
SERVED_STATUSES = frozenset({200, 401, 403})

# Port the REST API service listens on out of the box. It is configurable in the console,
# so it is a default rather than a certainty.
REST_PORT = 4443
DEFAULT_PORTS = (REST_PORT,)


class RestApiEndpoint(NamedTuple):
    """Where a server's REST API answers."""

    port: int
    api_version: str

    @property
    def base_url_suffix(self) -> str:
        """Port suffix for building a base URL, e.g. ":4443"."""
        return f":{self.port}"


def probe_url(base_url: str, version: str) -> str:
    """Build the URL this module probes for one API version."""
    return f"{base_url.rstrip('/')}{PROBE_PATH.format(version=version)}"


def newest_first(versions: Iterable[str]) -> list[str]:
    """Order API versions newest first, dropping any that are not recognizable.

    Versions look like "v8". Comparing the number rather than the string keeps a
    hypothetical "v10" above "v8" instead of below it.
    """

    def key(version):
        try:
            return int(version.lstrip("vV"))
        except (AttributeError, TypeError, ValueError):
            return None

    # Filter before sorting: an unrecognizable entry has no key to compare, and mixing
    # those into the sort raises rather than just ordering them last
    ranked = [(key(version), version) for version in versions]
    return [version for _, version in sorted((r for r in ranked if r[0] is not None), reverse=True)]


async def _serves(client, base_url: str, version: str, timeout: float):
    """Return the version if the server routes it, else None."""
    url = probe_url(base_url, version)
    try:
        response = await client.get(url, timeout=timeout)
    except Exception as err:
        _LOGGER.debug("%s did not answer: %s", url, err)
        return None

    if response.status_code in SERVED_STATUSES:
        return version

    _LOGGER.debug("%s returned HTTP %s", url, response.status_code)
    return None


async def detect_api_version(
    base_url: str,
    *,
    verify_ssl: bool = True,
    timeout: float = DEFAULT_TIMEOUT,
    versions: Sequence[str] | None = None,
    client: httpx.AsyncClient | None = None,
) -> str | None:
    """Return the newest API version this server serves and this package supports.

    Args:
        base_url: Server base URL, e.g. "https://vb365.example.com:4443".
        verify_ssl: Whether to verify the server certificate. Ignored when ``client`` is
            given, since the caller's client carries its own settings.
        timeout: Per-request timeout in seconds. Probes are concurrent.
        versions: Candidate versions. Defaults to everything this package can speak.
        client: An existing httpx.AsyncClient to reuse instead of opening one.

    Returns:
        A version string such as "v8", or None if nothing answered — the caller should then
        fall back to a version it chooses.
    """
    candidates = newest_first(VERSION_TO_PACKAGE if versions is None else versions)
    if not candidates:
        return None

    owns_client = client is None
    if owns_client:
        client = httpx.AsyncClient(verify=verify_ssl)

    try:
        results = await asyncio.gather(
            *(_serves(client, base_url, version, timeout) for version in candidates),
            return_exceptions=True,
        )
    finally:
        if owns_client:
            await client.aclose()

    served = {result for result in results if isinstance(result, str)}
    if not served:
        _LOGGER.debug("No API version answered on %s", base_url)
        return None

    # candidates is newest-first, so the first match is the newest version served
    detected = next(version for version in candidates if version in served)
    _LOGGER.debug("%s serves %s; selected %s", base_url, sorted(served), detected)
    return detected


async def detect_rest_api(
    host: str,
    *,
    ports: Sequence[int] = DEFAULT_PORTS,
    versions: Sequence[str] | None = None,
    verify_ssl: bool = True,
    timeout: float = DEFAULT_TIMEOUT,
    client: httpx.AsyncClient | None = None,
) -> RestApiEndpoint | None:
    """Find where a server answers: which port, and which API version.

    The REST API service listens on 4443 by default but the port is configurable, so a
    caller that has been told "cannot connect" cannot assume the port is right. The probe
    URL contains the port, so one sweep answers both questions at once rather than detecting
    a port and then re-probing for a version.

    Args:
        host: Hostname or address, without scheme or port.
        ports: Candidate ports, in order of preference. The first that answers wins, so a
            caller with a non-default deployment should list its own port first.
        versions: Candidate versions. Defaults to everything this package can speak.
        verify_ssl: Whether to verify the server certificate. Ignored when ``client`` is
            given, since the caller's client carries its own settings.
        timeout: Per-request timeout in seconds. Probes are concurrent.
        client: An existing httpx.AsyncClient to reuse instead of opening one.

    Returns:
        A RestApiEndpoint(port, api_version), or None if nothing answered.
    """
    candidates = newest_first(VERSION_TO_PACKAGE if versions is None else versions)
    if not candidates or not ports:
        return None

    owns_client = client is None
    if owns_client:
        client = httpx.AsyncClient(verify=verify_ssl)

    attempts = [(port, version) for port in ports for version in candidates]

    try:
        results = await asyncio.gather(
            *(
                _serves(client, f"https://{host}:{port}", version, timeout)
                for port, version in attempts
            ),
            return_exceptions=True,
        )
    finally:
        if owns_client:
            await client.aclose()

    answered = {
        (port, version)
        for (port, version), result in zip(attempts, results)
        if isinstance(result, str)
    }
    if not answered:
        _LOGGER.debug("Nothing answered on %s across ports %s", host, list(ports))
        return None

    # ports is preference-ordered and candidates is newest-first, so the first hit in that
    # nesting is the preferred port running its newest served version
    port, version = next(attempt for attempt in attempts if attempt in answered)
    _LOGGER.debug(
        "%s answered on %s; selected port %s with %s",
        host,
        sorted(answered),
        port,
        version,
    )
    return RestApiEndpoint(port=port, api_version=version)
