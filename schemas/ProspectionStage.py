from pydantic import BaseModel, ConfigDict
from typing import Optional


class ProspStageBase(BaseModel):
    user_id: Optional[str] = None
    client_id: str
    source: str #"Referral", "Cold Call", "Website Inquiry", "Walk-in", "Global Introduction"
    stage: str
    entry_date: str
    notes: Optional[str] = None

class ProspStageCreate(ProspStageBase):
    pass


class ProspStageResult(ProspStageBase):
    # id:str
    model_config = ConfigDict(from_attributes=True)