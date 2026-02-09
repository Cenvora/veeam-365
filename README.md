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
        api_version="v8"
    )

    await vc.connect()

    # use the client...

    await vc.close()

asyncio.run(main())
```

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
