"""
HTTPClient abstraction over requests or httpx.
"""
from typing import Any, Dict
from sdk.common.logging import get_logger
from sdk.common.types import RateLimitInfo, KeyInfo
from sdk.exceptions.errors import HTTPError

logger = get_logger(__name__)

class HTTPClient:
    """Simple HTTP client wrapper."""
    def __init__(self, adapter: str = "httpx"):
        self.adapter = adapter

    def get(self, url: str, headers: Dict[str, str] = None) -> Any:
        """Sends a GET request."""
        # TODO: implement HTTP GET logic
        raise NotImplementedError

    def post(self, url: str, json: Dict[str, Any] = None, headers: Dict[str, str] = None) -> Any:
        """Sends a POST request."""
        # TODO: implement HTTP POST logic
        raise NotImplementedError
