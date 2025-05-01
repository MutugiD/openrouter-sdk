"""
RequestDispatcher orchestrates API calls, rate-limits, and rotation.
"""
from sdk.client.auth import AuthService
from sdk.client.http_client import HTTPClient
from sdk.core.rate_limiter import RateLimitWatcher
from sdk.core.rotation_policy import RotationPolicy
from sdk.common.logging import get_logger
from sdk.common.metrics import MetricsCollector
from sdk.exceptions.errors import RateLimitError, AuthError

logger = get_logger(__name__)
metrics = MetricsCollector()

class RequestDispatcher:
    """Dispatcher for sending requests to OpenRouter API with rotation."""
    def __init__(self, api_key: str, models: list = None):
        self.auth_service = AuthService(api_key)
        self.http_client = HTTPClient()
        self.rate_watcher = RateLimitWatcher()
        self.rotation_policy = RotationPolicy(models or [])

    def dispatch(self, method: str, path: str, **kwargs):
        """Dispatch an HTTP request with rotation logic."""
        # TODO: implement dispatch logic
        raise NotImplementedError
