"""
RateLimitWatcher parses rate-limit headers and blocks or raises errors.
"""
import threading
import time
from sdk.common.types import RateLimitInfo
from sdk.common.logging import get_logger
from sdk.exceptions.errors import RateLimitError

logger = get_logger(__name__)

class RateLimitWatcher:
    """Detects and handles rate limit events."""
    def check(self, response):
        """Check response for rate limits."""
        raise NotImplementedError

    def wait_if_needed(self):
        """Sleep until rate limit resets, if applicable."""
        raise NotImplementedError
