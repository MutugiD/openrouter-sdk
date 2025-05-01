"""
Client module for OpenRouter SDK.
"""
from .dispatcher import RequestDispatcher
from .auth import AuthService, build_auth_header
from .http_client import HTTPClient
