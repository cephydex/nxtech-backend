from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from typing import Optional

class PolicyBase(BaseModel):
    start_date: str
    quote_id: str

class PolicyRequest(PolicyBase):
    duration: int

class PolicyCreate(BaseModel):
    start_date: str
    quote_id: str
    expiry_date: str
    created_by: str
    policy_type_id: str
    project_id: Optional[str] = None
    quote_props: Optional[str] = None
    insurance_company_id: str
    quote_amount: Decimal

class PolicyResult(PolicyCreate):
    id:str
    model_config = ConfigDict(from_attributes=True)