"""
RotationPolicy defines strategies for choosing next model.
"""
from abc import ABC, abstractmethod
from typing import List
from sdk.common.types import ModelMeta
from sdk.common.logging import get_logger

logger = get_logger(__name__)

class RotationPolicy(ABC):
    """Abstract base class for rotation policies."""
    def __init__(self, models: List[ModelMeta]):
        self.models = models

    @abstractmethod
    def choose_next(self) -> ModelMeta:
        """Select the next model based on policy."""
        pass

class RoundRobinPolicy(RotationPolicy):
    """Round-robin rotation."""
    def choose_next(self) -> ModelMeta:
        raise NotImplementedError
