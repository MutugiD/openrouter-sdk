"""
ModelRegistry holds metadata and usage for each model.
"""
import threading
from sdk.common.types import ModelMeta
from sdk.common.config import ConfigService
from sdk.common.logging import get_logger

logger = get_logger(__name__)

class ModelRegistry:
    """Registry for managing model exhaustion and usage."""
    def __init__(self, models=None):
        self._lock = threading.Lock()
        self._models = models or []

    def get_current(self):
        """Return the current model."""
        raise NotImplementedError

    def mark_exhausted(self, model_id: str):
        """Mark a model as exhausted."""
        raise NotImplementedError

    def update_usage(self, model_id: str, used: int):
        """Update usage metrics for a model."""
        raise NotImplementedError
