from pydantic import BaseModel, ConfigDict
from typing import Optional


class ProfessionBase(BaseModel):
    name: str
    group_id: str
    code: Optional[str] = None


class ProfessionCreate(ProfessionBase):
    pass


class ProfessionResult(ProfessionBase):
    id:str

    model_config = ConfigDict(from_attributes=True)


class ProfessionalGroupBase(BaseModel):
    name: str


class ProfessionalGroupCreate(ProfessionalGroupBase):
    pass


class ProfessionalGroupResult(ProfessionBase):
    id:str

    model_config = ConfigDict(from_attributes=True)

