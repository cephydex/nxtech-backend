from pydantic import BaseModel, ConfigDict
from typing import Optional


class PolicyTypeBase(BaseModel):
    cat_id: str
    name: str
    description: Optional[str] = None
    commission: Optional[float] = 0.00


class QuoteCreate(PolicyTypeBase):
    pass


class QuoteResult(PolicyTypeBase):
    id:str
    model_config = ConfigDict(from_attributes=True)
