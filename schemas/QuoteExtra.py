from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from decimal import Decimal


class QuoteExtraBase(BaseModel):
    insurance_company_id:str
    quote_id:Optional[str] = None
    created_by:Optional[str] = None
    extras:dict
    quote_amount: Decimal
    accepted:Optional[bool] = False


class QuoteExtraCreate(QuoteExtraBase):
    pass


# class QuoteExtraRequest(BaseModel):
#     quote_id:str
#     extras: List[QuoteExtraCreate]


class QuoteExtraResult(QuoteExtraBase):
    id:str
    model_config = ConfigDict(from_attributes=True)
