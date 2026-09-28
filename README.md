<h1 align="center">
<br>
<img src="https://raw.githubusercontent.com/Cenvora/veeam-365/main/media/Veeam_logo_2024_RGB_main_20.png"
     alt="Veeam Logo"
     height="100">
<br>
<br>
Veeam Backup for Microsoft 365 Python API Wrapper
</h1>

<h4 align="center">
Python package for interacting with the Veeam Backup for Microsoft 365 REST API
</h4>

<!-- Summary -->
This project is an independent, open source Python client for the Veeam Backup for Microsoft 365 <a href="https://helpcenter.veeam.com/references/vbo365/8/rest/tag/SectionAbout">REST API</a>. It is not affiliated with, endorsed by, or sponsored by Veeam Software.
<!-- Summary -->

## Supported Versions

<table>
  <thead>
    <tr>
      <th>VB365 Version</th>
      <th>API Version</th>
      <th>Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>8.0.2.159</td>
      <td>v8</td>
      <td style="text-align:center;">&#9989;</td>
    </tr>
    <tr>
      <td>7.0.0.2911</td>
      <td>v7</td>
      <td style="text-align:center;">&#9989;</td>
    </tr>
    <tr>
      <td>6.0.0.367</td>
      <td>v6</td>
      <td style="text-align:center;">&#9989;</td>
    </tr>
    <tr>
      <td>&lt; 6.0.0.367</td>
      <td>&lt; v6</td>
      <td style="text-align:center;">&#10060;</td>
    </tr>
  </tbody>
</table>

## How to support new API versions
1. Download the OpenAPI schema into openapi_schemas
2. Install the openapi-python-client package
3. Run `python fix_openapi.py .\openapi_schemas\vb365_rest_{version}.json .\openapi_schemas\vb365_rest_{version}_fixed.json` 
4. Run `openapi-python-client generate --path ".\openapi_schemas\vb365_rest_{version}_fixed.json" --output-path ".\veeam_365" --overwrite`
5. Fix any warnings/errors
6. Rename the folder to match the API version (i.e., `v8`)
7. Add the version mapping to versions.py
8. Write pytest tests
9. If an older API has been deprecated, delete its folder, json, and version.py entry, then update the supported versions section of the readme

## Install
### From PyPi
`pip install veeam-365`

### From Source
Clone the repository and install dependencies:
```sh
git clone https://github.com/Cenvora/veeam-365.git
cd veeam-365
pip install -e .
```

## Usage
### Recommended Usage (Smart Client)
The `VeeamClient` handles:
- API version routing
- Authentication
- Token refresh
- Async calls
- Operation discovery

Each packaged version can be called independently through separate imports, but this is the <strong>recommended way</strong>  to use this library.

#### Create a client and connect
```python
import asyncio
from veeam_365.client import VeeamClient

async def main():
    vc = VeeamClient(
        host="https://vb365.example.com:4443",
        username="administrator",
        password="SuperSecretPassword",
        verify_ssl=False,
        api_version="v8",
        disable_antiforgery_token=True
    )

    await vc.connect()

    # use the client...

    await vc.close()

asyncio.run(main())
```

The client is also an async context manager, which closes it on exit:

```python
async with VeeamClient(host=..., username=..., password=..., api_version="v8") as vc:
    await vc.connect()
    ...
```

**Optional Parameters:**
- `verify_ssl` (bool | `ssl.SSLContext` | str, default: `True`): Enable/disable SSL certificate verification, or pass an `ssl.SSLContext` or a CA bundle path
- `timeout` (float | `httpx.Timeout` | None, default: `30.0`): Timeout for every request, in seconds. `None` disables timeouts.
- `disable_antiforgery_token` (bool, default: `True`): Disable antiforgery token requirement. Set to `True` for programmatic/API clients (recommended). Set to `False` only if using browser-based authentication with cookies.

#### Detect the API version a server serves

The REST API has no endpoint that reports its supported versions, and nothing negotiates one
for you — the version is part of every path, so a client picks one up front. That path is
also what makes detection possible: `/{version}/ServiceInstance` exists in every version and
requires a token, so an anonymous probe gets 401 where the version is served and 404 where it
is not. `detect_api_version` returns the newest version that both the server serves and this
library can speak:

```python
import asyncio
from veeam_365.client import VeeamClient
from veeam_365.discovery import detect_api_version

async def main():
    base_url = "https://vb365.example.com:4443"

    api_version = await detect_api_version(base_url, verify_ssl=False)
    if api_version is None:
        # The server may be unreachable or behind a proxy — choose your own default
        api_version = "v8"

    vc = VeeamClient(
        host=base_url,
        username="administrator",
        password="SuperSecretPassword",
        api_version=api_version,
        verify_ssl=False,
    )
    await vc.connect()

asyncio.run(main())
```

Detection needs no credentials, so it can run before you have any. Probes are concurrent, so
it costs roughly one round trip regardless of how many versions this library supports.

If you do not know the port either, `detect_rest_api` finds both at once. The REST API
service listens on 4443 out of the box, but the port is configurable in the console, so pass
your own candidates when a deployment uses something else:

```python
from veeam_365.discovery import detect_rest_api

endpoint = await detect_rest_api("vb365.example.com", verify_ssl=False)
if endpoint:
    print(endpoint.port, endpoint.api_version)  # e.g. 4443 v8
    base_url = f"https://vb365.example.com{endpoint.base_url_suffix}"
```

Ports are tried in preference order and the newest version served by the winning port is
returned.

Resolve it once and store the result rather than detecting on every start: a server upgrade
would otherwise silently move you onto a newer version, and versions rename enum values and
add required fields.

#### Call an API endpoint (async)
```python
repos = await vc.call(
  vc.api("backup_repository").backup_repository_get_repositories
)

# repos is a PageOfRESTBackupRepository model
for repo in repos.data or []:
  print(repo.name)
```

#### Call any endpoint
Operations map directly to the OpenAPI layout:
```markdown
api/
└── backup_repository/
  └── backup_repository_get_repositories.py
```

Call it like this:
```python
await vc.call(
    vc.api("backup_repository").backup_repository_get_repositories
)
```

Or explicity:
```python
await vc.call(
    vc.api("backup_repository.backup_repository_get_repositories")
)
```

#### Pagination example
```python
result = await vc.call(
  vc.api("backup_repository").backup_repository_get_repositories,
    limit=50,
    offset=0,
)
```

#### Close the client
```python
await vc.close()
```

`close()` drops the session and closes the underlying HTTP connections. `async with` does this for you.

#### Errors

`VeeamClient` authenticates on first use and refreshes its token as it expires. When the
refresh token is refused it falls back to the password grant. Concurrent calls share a
single refresh.

| Exception | Meaning |
|---|---|
| `veeam_365.exceptions.VeeamAuthenticationError` | The server refused the username/password at login. Ask for new credentials. |
| `veeam_365.exceptions.VeeamSessionError` | The session was rejected mid-use (the server answered with an undecodable, usually empty, body). The session has been dropped; the next call logs in again. The operation is **not** retried. |
| `httpx.HTTPError`, `OSError`, `TimeoutError` | The server could not be reached, timed out, or answered the login with a 5xx/429. Retry later. These are never wrapped. |

Both Veeam exceptions subclass `veeam_365.exceptions.VeeamError` and `PermissionError`.
A documented error response from an endpoint (such as a 404) is returned as a
`RESTExceptionInfo` model rather than raised.

```python
import httpx
from veeam_365.exceptions import VeeamAuthenticationError, VeeamSessionError

try:
    result = await vc.call(vc.api("backup_repository").backup_repository_get_repositories)
except VeeamAuthenticationError:
    ...  # bad credentials: prompt the user
except VeeamSessionError:
    ...  # transient: the next call re-authenticates
except (httpx.HTTPError, OSError, TimeoutError):
    ...  # server unreachable
```

## Contributing
Contributions are welcome! To contribute:
- Fork the repository
- Create a feature branch
- Make your changes and add tests
- Submit a pull request with a clear description

Please follow PEP8 style and include docstrings for new functions/classes.

## 🤝 Core Contributors
This project is made possible thanks to the efforts of our core contributors:

- [Jonah May](https://github.com/JonahMMay)  
- [Maurice Kevenaar](https://github.com/mkevenaar)  

We’re grateful for their continued support and contributions.
