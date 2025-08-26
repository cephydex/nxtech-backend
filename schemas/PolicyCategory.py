from pydantic import BaseModel, ConfigDict
from typing import Optional


class PolicyCategoryBase(BaseModel):
    name: str
    description: Optional[str] = None



class PolicyCategoryCreate(PolicyCategoryBase):
    pass


class PolicyCategoryResult(PolicyCategoryBase):
    id:str
    model_config = ConfigDict(from_attributes=True)
