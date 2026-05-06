
""" A client library for accessing Veeam Backup for Microsoft 365 REST API """
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
