from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

class Indicator(BaseModel):
    ioc_type: str
    value: str
    first_seen: Optional[datetime] = None
    last_seen: Optional[datetime] = None
    source: str
    confidence: int = Field(ge=0, le=100, default=60)
    tags: List[str] = []
    ttps: List[str] = []
    metadata: Dict = {}
