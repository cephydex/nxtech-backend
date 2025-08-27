from pydantic import BaseModel, ConfigDict
from typing import Optional
# from decimal import Decimal


class IndividualProspBase(BaseModel):
    title_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    other_names: Optional[str] = None
    # dob: Optional[str] = None
    sex: Optional[str] = 'F'
    nationality_id: Optional[str] = None


class ProspectBase(IndividualProspBase):
    client_type: Optional[str] = None
    company_name: Optional[str] = None
    year_of_inc: Optional[str] = None
    address_loc: str
    email: str
    contact_no: str
    created_by: Optional[str] = None
    notes: Optional[str] = None
    stage: str
    source: Optional[str] = None
    active_status: Optional[str] = 'active'


class ProspectCreateWProduct(ProspectBase):
    policy_type_id: Optional[str] = None

class ProspectCreate(ProspectBase):
    pass


class ProspectResult(ProspectBase):
    id:str
    model_config = ConfigDict(from_attributes=True)



class ProspectionStageBase(BaseModel):
    created_by: str
    project_id: str
    stage: str
    notes: Optional[str] = None

class ProspectionStageCreate(ProspectionStageBase):
    pass

class ProspectionStageResult(ProspectionStageBase):
    id:str
    model_config = ConfigDict(from_attributes=True)


class ProspectContactBase(BaseModel):
    prospect_id: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    contact_no: Optional[str] = None
    role: Optional[str] = None
    created_at: Optional[str] = None

class ProspectContactCreate(ProspectContactBase):
    pass


class ProspectContactResult(ProspectContactBase):
    id:str
    model_config = ConfigDict(from_attributes=True)
