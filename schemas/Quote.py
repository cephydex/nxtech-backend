from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal


class QuoteBase(BaseModel):
    project_id: str
    policy_type_id: str
    created_by: Optional[str] = None
    prospect_id: Optional[str] = None
    insurance_company_id: Optional[str] = None
    premium: Decimal
    currency: Optional[str] = 'GHS'
    entry_data: dict
    status: str
    valid_until: Optional[str] = None
    document_url: Optional[str] = None


class QuoteCreate(QuoteBase):
    pass


class QuoteResult(QuoteBase):
    id:str
    model_config = ConfigDict(from_attributes=True)
