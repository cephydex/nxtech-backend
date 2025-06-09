from pydantic import BaseModel, ConfigDict
from typing import Optional


class DepartmentBase(BaseModel):
    name: str
    description: Optional[str] = None
    code: Optional[str] = None


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResult(DepartmentBase):
    id:str

    model_config = ConfigDict(from_attributes=True)

