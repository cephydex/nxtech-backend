from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal


class IndividualClientBase(BaseModel):
    title_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    other_names: Optional[str] = None
    dob: Optional[str] = None
    sex: Optional[str] = 'F'
    nationality_id: Optional[str] = None
    id_type: Optional[str] = None
    id_number: Optional[str] = None
    pep: Optional[bool] = False
    residential_addr: Optional[str] = None
    profession_id: Optional[str] = None

class ClientBase(IndividualClientBase):
    client_type: Optional[str] = None
    client_code: Optional[str] = None
    company_name: Optional[str] = None
    company_reg_no: Optional[str] = None
    year_of_inc: Optional[str] = None

    address_loc: str
    email: str
    contact_no: str
    is_existing: Optional[bool] = False
    uploaded_doc: Optional[str] = None
    tin_no: str
    active_status: Optional[str] = 'active'
    notes: Optional[str] = None
    account_manager: Optional[str] = None
    claims_manager: Optional[str] = None
    created_by: Optional[str] = None
    login_id: Optional[str] = None
    professional_group_id: Optional[str] = None
    postal_addr: Optional[str] = None


class ClientCreate(ClientBase):
    pass


class ClientResult(ClientBase):
    id:str
    model_config = ConfigDict(from_attributes=True)

# client_type, company_name, address_loc, email, contact_no, is_existing, client_code, company_reg_no, year_of_inc, 
# uploaded_doc, tin_no, active_status, notes, 
# account_manager, claims_manager, created_by,
# title_id, first_name, last_name, other_names, dob, sex, nationality_id, id_type, id_number, pep, 
# residential_addr, postal_addr, professional_group_id, profession_id,

class ClientContactBase(BaseModel):
    client_id: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    contact_no: Optional[str] = None
    role: Optional[str] = None

class ClientContactCreate(ClientContactBase):
    pass


class ClientContactResult(ClientContactBase):
    id:str
    model_config = ConfigDict(from_attributes=True)