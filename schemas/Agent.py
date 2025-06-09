from pydantic import BaseModel, ConfigDict
from typing import Optional


class AgentBase(BaseModel):
    title_id: str
    first_name: str
    last_name: str
    email: str
    mobile_no: str
    address: str
    company_name: Optional[str] = None
    user_id: Optional[str] = None


class AgentCreate(AgentBase):
    pass


class AgentResult(AgentBase):
    id:str

    model_config = ConfigDict(from_attributes=True)

