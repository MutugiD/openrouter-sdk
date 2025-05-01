"""
Custom exception hierarchy for the SDK.
"""
class SDKError(Exception):
    """Base class for SDK errors."""
    pass

class AuthError(SDKError):
    """Authentication-related errors."""
    pass

class RateLimitError(SDKError):
    """Rate limit exceeded."""
    pass

class HTTPError(SDKError):
    """HTTP request failed."""
    pass

class RetryError(SDKError):
    """Retry logic failed."""
    pass

class ConfigError(SDKError):
    """Configuration loading failed."""
    pass
