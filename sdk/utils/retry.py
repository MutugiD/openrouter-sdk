"""
Retry helper with exponential backoff.
"""
import time
import random
from typing import Callable, Any
from sdk.exceptions.errors import RetryError

def retry(func: Callable[..., Any], retries: int = 3, backoff: float = 0.5) -> Any:
    """Retry a function with exponential backoff."""
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            return func()
        except Exception as e:
            last_exc = e
            sleep_time = backoff * (2 ** (attempt - 1))
            time.sleep(sleep_time + random.random() * 0.1)
    raise RetryError(f"Function failed after {retries} retries") from last_exc
