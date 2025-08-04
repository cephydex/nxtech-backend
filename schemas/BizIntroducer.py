from pydantic import BaseModel, ConfigDict, root_validator, model_validator
from typing import Optional
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)


class BizIntroducerBase(BaseModel):
    title_id: Optional[ str] = None
    full_name: Optional[ str] = None
    primary_contact: Optional[ str] = None
    email: str
    contact_no: str
    address: Optional[str] = None
    location: Optional[str] = None

    business_name: Optional[str] = None
    business_reg_no: Optional[str] = None
    id_type: Optional[str] = None
    id_number: Optional[str] = None
    tin_no: Optional[str] = None
    user_id: Optional[str] = None
    commission_rate: Optional[Decimal] = 1.00

    bank_id: Optional[str] = None
    bank_account_name: Optional[str] = None
    bank_branch_name: Optional[str] = None
    bank_account_no: Optional[str] = None
    notes: Optional[str] = None
    commission_rate: Optional[float] = 1.00
    biz_agreement_doc: Optional[str] = None
    itype: Optional[str] = 'Individual'

    # @model_validator(mode="after")
    # def validate_business_fields(cls, values):
    #     biz_regno = values.get("business_reg_no")
    #     prim_contact = values.get("primary_contact")
    #     tin = values.get("tin_no")
    #     title = values.get("title_id")
    #     name = values.get("full_name")
    #     id_type = values.get("id_type")
    #     id_num = values.get("id_number")

    #     if values.get("itype") == "Corporate":
    #         missing_fields = []
    #         if not values.get("business_name"):
    #             missing_fields.append("business_name")
    #         if not values.get("business_reg_no"):
    #             missing_fields.append("business_reg_no")
    #         if not values.get("primary_contact"):
    #             missing_fields.append("primary_contact")
    #         if not values.get("tin_no"):
    #             missing_fields.append("tin_no")
    #         if missing_fields:
    #             raise ValueError(f"Missing required fields for Corporate account: {', '.join(missing_fields)}")
            
    #     elif values.get("itype") == "Individual":
    #         missing_fields = []
    #         if not values.get("title_id"):
    #             missing_fields.append("title_id")
    #         if not values.get("full_name"):
    #             missing_fields.append("full_name")
    #         if not values.get("id_type"):
    #             missing_fields.append("id_type")
    #         if not values.get("id_number"):
    #             missing_fields.append("id_number")
    #         if missing_fields:
    #             raise ValueError(f"Missing required fields for Individual account: {', '.join(missing_fields)}")
    #     return values




class BizIntroducerCreate(BizIntroducerBase):

    # @model_validator(mode="after")
    # def validate_fields(cls, values):
        
    #     # biz_regno = values.get("business_reg_no")
    #     logger.debug('We sure have valication')
    #     logger.debug(values)
        # prim_contact = values.get("primary_contact")
        # tin = values.get("tin_no")
        # title = values.get("title_id")
        # name = values.get("full_name")
        # id_type = values.get("id_type")
        # id_num = values.get("id_number")

        # if values.get("itype") == "Corporate":
        #     missing_fields = []
        #     if not values.get("business_name"):
        #         missing_fields.append("business_name")
        #     if not values.get("business_reg_no"):
        #         missing_fields.append("business_reg_no")
        #     if not values.get("primary_contact"):
        #         missing_fields.append("primary_contact")
        #     if not values.get("tin_no"):
        #         missing_fields.append("tin_no")
        #     if missing_fields:
        #         raise ValueError(f"Missing required fields for Corporate account: {', '.join(missing_fields)}")
            
        # elif values.get("itype") == "Individual":
        #     missing_fields = []
        #     if not values.get("title_id"):
        #         missing_fields.append("title_id")
        #     if not values.get("full_name"):
        #         missing_fields.append("full_name")
        #     if not values.get("id_type"):
        #         missing_fields.append("id_type")
        #     if not values.get("id_number"):
        #         missing_fields.append("id_number")
        #     if missing_fields:
        #         raise ValueError(f"Missing required fields for Individual account: {', '.join(missing_fields)}")
        # return values
    pass


class BizIntroducerResult(BizIntroducerBase):
    id:str
    model_config = ConfigDict(from_attributes=True)

# title_id, full_name, primary_contact, email, contact_no, address, location, id_type, id_number, business_name, business_reg_no, tin_no
# , bank_id, bank_account_name, bank_branch_name, bank_account_no, commission_rate, biz_agreement_doc, user_id, itype, notes