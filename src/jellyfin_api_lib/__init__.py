"""A client library for accessing Jellyfin API"""

from .client import AuthenticatedClient, Client
from .extra_clients import HeaderClient, KeyClient, UserPassClient

__all__ = ("AuthenticatedClient", "Client", "HeaderClient", "KeyClient", "UserPassClient")
