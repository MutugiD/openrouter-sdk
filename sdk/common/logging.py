"""
Structured logging setup for the SDK.
"""
import logging
from typing import Any, Dict

def get_logger(name: str) -> logging.Logger:
    """Return a configured logger."""
    logger = logging.getLogger(name)
    # TODO: configure handler/formatter
    return logger
