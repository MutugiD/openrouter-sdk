"""
Shared data models for the SDK.
"""
from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class RateLimitInfo:
    requests: int
    interval: str

@dataclass
class KeyInfo:
    label: str
    usage: int
    limit: Optional[int]
    is_free_tier: bool
    rate_limit: RateLimitInfo

@dataclass
class ModelMeta:
    model_id: str
    daily_limit: int
    rate_limit_per_minute: int
    is_free_tier: bool

@dataclass
class Config:
    api_key: str
    models: Dict[str, ModelMeta]
