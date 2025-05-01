"""
ConfigService loads SDK configurations from JSON, YAML, or environment.
"""
import os
import json
import yaml
from sdk.common.types import Config
from sdk.exceptions.errors import ConfigError

class ConfigService:
    """Service for loading configuration."""
    def __init__(self, path: str = None):
        raise NotImplementedError
