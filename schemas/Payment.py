# from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Any
# from uuid import UUID

class PaymentRequestSchema(BaseModel):
    # quote_id: UUID
    # created_by: User
    phone_no: str
    description: Optional[str] = None

class PaymentHubtelCallback(BaseModel):
    ResponseCode: str
    Status: Optional[str] = None
    Data: Any