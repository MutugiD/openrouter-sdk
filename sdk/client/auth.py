"""
AuthService and helper to build auth headers.
"""
from typing import Dict
from sdk.common.config import ConfigService
from sdk.common.logging import get_logger
from sdk.exceptions.errors import AuthError

logger = get_logger(__name__)

def build_auth_header(api_key: str) -> Dict[str, str]:
    """Builds the Authorization header for a given API key."""
    if not api_key:
        raise AuthError("API key is required")
    return {"Authorization": f"Bearer {api_key}"}

class AuthService:
    """Service for handling authentication."""
    def __init__(self, api_key: str):
        self.api_key = api_key

    @property
    def auth_header(self) -> Dict[str, str]:
        return build_auth_header(self.api_key)
