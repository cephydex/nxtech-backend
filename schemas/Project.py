from pydantic import BaseModel, ConfigDict
from typing import Optional
# from decimal import Decimal


class ProjectBase(BaseModel):
    prospect_id: str
    policy_type_id: Optional[str] = None
    status: Optional[str] = None
    created_by: str


class ProjectCreate(ProjectBase):

    def __str__(self):
        return f"Project(prospect_id='{self.prospect_id}', policy_type_id='{self.policy_type_id}', status={self.status})"

    def __repr__(self):
        return f"Project(prospect_id='{self.prospect_id}', policy_type_id='{self.policy_type_id}', status={self.status})"


class ProjectResult(ProjectBase):
    id:str
    model_config = ConfigDict(from_attributes=True)
