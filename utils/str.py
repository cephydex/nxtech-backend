import logging
from repos.client import ClientRepo

logger = logging.getLogger(__name__)

def fmtPhoneNumber(phone_no: str):
    if phone_no[0:1] == '0':
        phone_no = '233'+ phone_no[1:]

    return phone_no


def getNextMemberId():
    lastId = ClientRepo.getLastClientId()
    # print('TEMP', lastId)
    member_id = None
    prefix = "NXT"
    if lastId and lastId['client_code']:
        old_id = lastId['client_code']
        member_id = processNewClientId(old_id, prefix)
    else:
        member_id = f"{prefix}00001"
    
    return member_id


def processNewClientId(old_id:str, prefix:str):
    num_part = int(old_id[3:])
    logger.warning("PROC 1: mID %s -- %d" % (old_id, num_part))
    num_part += 1
    num_str = f'{num_part:05d}'
    new_id = prefix + num_str
    logger.warning("PROC 2: mID %s -- %d" % (new_id, num_part))
    return new_id