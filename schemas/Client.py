from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal


class ClientBase(BaseModel):
    title_id: str
    first_name: str
    last_name: str
    other_names: Optional[str] = None
    email: str
    mobile_no: str
    mobile_no2: Optional[str] = None
    tel_no: Optional[str] = None
    address: str
    dob: str
    marital_status: Optional[str] = 'married'
    address2: Optional[str] = None
    company_name: Optional[str] = None
    active_status: Optional[str] = None
    created_by: Optional[str] = None
    login_id: Optional[str] = None
    location: Optional[str] = None
    agent_id: Optional[str] = None
    biz_intro_id: Optional[str] = None
    professional_group_id: Optional[str] = None
    profession_id: Optional[str] = None
    account_no: Optional[str] = None
    driver_license_cat: Optional[str] = None
    driver_license_no: Optional[str] = None
    nationality_id: str
    national_id: str
    # share_percentage: Optional[Decimal] = 1.00
    
    # title_id, first_name, last_name, other_names
    # , address, address2, email, mobile_no, mobile_no2, tel_no
    # , dob, company_name, marital_status, active_status, professional_group_id, profession_id, nationality_id, 
    # , driver_license_cat, driver_license_no, account_no, national_id (ghana_card)


class ClientCreate(ClientBase):
    pass


class ClientResult(ClientBase):
    id:str

    model_config = ConfigDict(from_attributes=True)

