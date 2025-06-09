from schemas.User import (
        # RoleCreate, RoleResult, 
        UserCreate, UserResult, UserUpdateProfile
    )
# from models.UserRole import UserRole
from models.User import User
import uuid, logging, traceback
from typing import List


logger = logging.getLogger(__name__)


class UserRepo:

    async def create(user: UserCreate):
        res = {
            "errors": {},
            "data": None
        }

        try:
            db_item= User()
            db_item.id= str(uuid.uuid4())
            db_item.last_name= user.email
            db_item.first_name= user.username
            db_item.sex= user.active_status
            
            db_item.role_id= str(user.role_id)
            db_item.save()
            res['data'] = db_item
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("User %s already exists" % user.username+' | '+user.email)
                res['errors']["unique_constraint"] = str(ex)
            logger.error("CREATE ERR :: %s" % str(ex))
            traceback.print_exc()

        return res


    async def update_profile(id:str, user: UserUpdateProfile):
        res = {
            "errors": {},
            "data": None
        }

        upd_data = {
            "username": user.username,
            "email": user.email,
        }
        # if user.active_status:
        #     upd_data["active_status"] = user.active_status

        try:
            db_res = User.find(id) \
                        .update(upd_data)
        
            res['data'] = db_res.serialize()
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("User %s already exists" % user.username+' '+user.email)
                res['errors']["unique_constraint"] = str(ex)
            logger.error("CREATE ERR :: %s" % str(ex))
            traceback.print_exc()

        return res


    async def change_password(id:str, new_password:str):
        res = {
            "errors": {},
            "data": None
        }

        try:
            db_res = User.find(id).update({"password":new_password,})
            res['data'] = db_res.serialize()
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("User %s password could not be updated" % db_res.username+' '+db_res.email)
                res['errors']["unique_constraint"] = str(ex)
            logger.error("CREATE ERR :: %s" % str(ex))
            traceback.print_exc()

        return res

    
    def fetch_by_id_min(id:str) -> UserResult:
        res = User.where('id', '=', id) \
                .get(["username", "active_status", "email", "created_at",]) \
                .first()

        return res


    def fetch_by_email(email:str) -> UserResult:
        res = User.by_email(email) \
            .with_("role") \
            .first()
        
        return res


    # def fetch_all() -> List[AdminResult]:
    #     res = Role.all()
    #     all_data = [x.as_dict() for x in res]
    #     # print("serialized", all_data)
    #     # check_data = all_vehicles = [{"vehicle": x.vehicle} for x in vehicle_sum]

    #     return all_data
    

    # def fetch_by_phone(phone:str) -> AdminResult:
    #     res = Admin.by_phone(phone)
    #     # all_data = [x.as_dict() for x in res]
    #     # print("serialized", all_data)
    #     # check_data = all_vehicles = [{"vehicle": x.vehicle} for x in vehicle_sum]
    #     return res


# class RoleRepo:

#     async def create(role: RoleCreate) -> RoleResult:
#         try:
#             db_item= Role()
#             db_item.id= str(uuid.uuid4())
#             db_item.name= role.name
#             db_item.description= role.description
#             db_item.save()
#         except Exception as ex:
#             if 'unique constraint' in str(ex):
#                 logger.error("Role %s already exists" % role.name)
#             logger.error(str(ex))
#         return db_item


#     def fetch_all() -> List[RoleResult]:
#         res = Role.all()
#         all_data = [x.as_dict() for x in res]
#         # print("serialized", all_data)
#         # check_data = all_vehicles = [{"vehicle": x.vehicle} for x in vehicle_sum]

#         return all_data


#     def find_by_id(id:str) -> RoleResult:
#         res = Role.where('id', id).get()
#         all_data = [x.as_dict() for x in res]

#         return all_data


#     def update1(id:str, data:RoleCreate) -> RoleResult:
#         res = Role.find(id) \
#             .update(name=data.name, description=data.description)
#         return res


#     def update1(id:str, data:RoleCreate) -> RoleResult:
#         item = Role.find(id)
#         item.name= data.name
#         item.description= data.description

#         item.save()
#         return item
