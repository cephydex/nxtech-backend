from pydantic import BaseModel, ConfigDict
from typing import List


class QuoteExtraBase(BaseModel):
    # quote_id:str
    description:str 
    type:str


class QuoteExtraCreate(QuoteExtraBase):
    pass


class QuoteExtraRequest(BaseModel):
    quote_id:str
    extras: List[QuoteExtraCreate]


class QuoteExtraResult(QuoteExtraBase):
    id:str
    model_config = ConfigDict(from_attributes=True)
