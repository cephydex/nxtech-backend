from pydantic import BaseModel, ConfigDict
from typing import Optional


class InsuranceCompanyBase(BaseModel):
    # name, company_type, head_office_addr, contact_no, nic_license_no, biz_reg_no, tin_no
    # parnership_type, bank_id, bank_account_name, bank_account_no
    name: str
    company_type: Optional[str] = "Non Life"
    head_office_addr: Optional[str] = None
    contact_no: Optional[str] = None
    nic_license_no: Optional[str] = None
    biz_reg_no: Optional[str] = None
    tin_no: Optional[str] = None
    parnership_type: Optional[str] = None


class DepartmentCreate(InsuranceCompanyBase):
    pass


class DepartmentResult(InsuranceCompanyBase):
    id:str

    model_config = ConfigDict(from_attributes=True)

