from typing import Optional
from pydantic import BaseModel


class MinResponse():
    pass


class GenResponse(BaseModel):

    def __init__(self, message, status_code, data=None) -> None:
        super().__init__(message=message, status_code=status_code, data=data)
        self.message = message
        self.status_code = status_code
        self.data = data

    def __repr__(self):
        return '(message=%s, code_status=%s, data=%s)' % (self.message, self.status_code, self.data,)

    message:str
    data:Optional[dict | list] = []
    status_code:int


def get_obj_attribs(db_user: any):
    attrs = vars(db_user)
    # now dump this in some way or another
    print(', '.join("%s: %s" % item for item in attrs.items()))


# attributes = [attr for attr in dir(db_user) 
#             if not attr.startswith('__') or not attr.startswith('_')]
# print("NEW APPR", attributes)
