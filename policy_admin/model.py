from pydantic import BaseModel, ConfigDict

class PolicyCreate(BaseModel):
    id:str
    quote_id: str
    start_date: str
    expiry_date: str
    created_by: str
    policy_type_id: str
    project_id: str
    quote_props: str

class PolicyResult(PolicyCreate):
    id:str
    model_config = ConfigDict(from_attributes=True)