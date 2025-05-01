"""
MetricsCollector for counting and gauging SDK events.
"""
from sdk.common.config import ConfigService

class MetricsCollector:
    """Collects SDK metrics."""
    def increment(self, name: str, amount: int = 1):
        """Increment a counter."""
        raise NotImplementedError

    def gauge(self, name: str, value: float):
        """Record a gauge metric."""
        raise NotImplementedError
