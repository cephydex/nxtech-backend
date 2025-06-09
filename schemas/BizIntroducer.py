from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal


class BizIntroducerBase(BaseModel):
    title_id: str
    first_name: str
    last_name: str
    email: str
    mobile_no: str
    address: str
    company_name: Optional[str] = None
    user_id: Optional[str] = None
    location: Optional[str] = None
    share_percentage: Optional[Decimal] = 1.00


class BizIntroducerCreate(BizIntroducerBase):
    pass


class BizIntroducerResult(BizIntroducerBase):
    id:str

    model_config = ConfigDict(from_attributes=True)

