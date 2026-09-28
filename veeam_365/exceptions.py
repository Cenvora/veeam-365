"""Exceptions raised by :class:`veeam_365.client.VeeamClient`.

Both concrete errors subclass :class:`PermissionError`, so code written against the older
behaviour (which raised a bare ``PermissionError``) keeps working. Transport failures
(``httpx.HTTPError``, ``OSError``, ``TimeoutError``) are never wrapped in these: they
propagate as-is so a caller can tell "server unreachable" from "credentials refused".
"""


class VeeamError(Exception):
    """Base class for errors raised by the Veeam client wrapper."""


class VeeamAuthenticationError(VeeamError, PermissionError):
    """The server refused the credentials at password login.

    Raised when the password grant returns something other than a token. This is the
    signal to ask the user for new credentials.
    """


class VeeamSessionError(VeeamError, PermissionError):
    """The session was rejected while in use.

    Raised when a response could not be decoded, which is how the server answers a
    rejected token (an empty body). The session has been dropped and the next call
    authenticates again. This is not proof that the credentials are wrong.
    """


__all__ = ["VeeamError", "VeeamAuthenticationError", "VeeamSessionError"]
