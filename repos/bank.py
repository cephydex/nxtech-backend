from typing import List
from models.Bank import Bank
from schemas.Bank import  BankCreate, BankResult
import logging, uuid

logger = logging.getLogger(__name__)

class BankRepo:
        
    # async def create(bank: BankCreate):
    #     res = {
    #         "errors": {},
    #         "data": None
    #     }

    #     try:
    #         db_item = Bank()
    #         db_item.id=str(uuid.uuid4())
    #         db_item.name=bank.name
    #         db_item.code=bank.code
    #         db_item.save()
    #         res['data'] = db_item.serialize()
            
    #     except Exception as ex:
    #         if 'unique constraint' in str(ex):
    #             logger.error("Bank %s already exists" % bank.name)
    #             res['errors']["unique_constraint"] = str(ex)
    #         logger.error(str(ex))
        
    #     return res


    def fetch_by_id(id: str):
        result = Bank.find(id)
        
        return result


    async def delete(id: str):
        result = Bank.find(id).delete()
        
        return result


    def fetch_all() -> List[BankResult]:
        result = Bank.all()
        
        return result.serialize()