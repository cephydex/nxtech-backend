from schemas.Auth import (
        # RoleCreate, RoleResult, 
        AdminCreate, AdminResult, AdminUpdateProfile
    )
from models.UserRole import UserRole as Role
from models.Admin import Admin
import uuid, logging, traceback
from typing import List


logger = logging.getLogger(__name__)


class AdminRepo:

    async def create(admin: AdminCreate):
        res = {
            "errors": {},
            "data": None
        }

        id = str(uuid.uuid4())
        try:
            db_item= Admin()
            db_item.id= id
            db_item.last_name= admin.last_name
            db_item.first_name= admin.first_name
            db_item.other_names= admin.other_names
            db_item.sex= admin.sex
            db_item.email= admin.email
            db_item.phone= admin.phone
            db_item.active_status= admin.active_status
            db_item.password= admin.password
            db_item.role_id= str(admin.role_id)
            db_item.inst= admin.inst
            db_item.save()
            res['data'] = db_item
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Admin %s already exists" % admin.first_name+' '+admin.last_name)
                res['errors']["unique_constraint"] = str(ex)
            logger.error("CREATE ERR :: %s" % str(ex))
            traceback.print_exc()

        return res


    async def update_profile(id:str, admin: AdminUpdateProfile):
        res = {
            "errors": {},
            "data": None
        }

        upd_data = {
            "first_name": admin.first_name,
            "last_name": admin.last_name,
        }
        if admin.other_names:
            upd_data["other_names"] = admin.other_names

        if admin.phone:
            upd_data["phone"] = admin.phone

        try:
            db_res = Admin.find(id) \
                        .update(upd_data)
        
            res['data'] = db_res.serialize()
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Admin %s already exists" % admin.first_name+' '+admin.last_name)
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
            db_res = Admin.find(id).update({"password":new_password,})
            res['data'] = db_res.serialize()
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Admin %s password could not be updated" % db_res.first_name+' '+db_res.last_name)
                res['errors']["unique_constraint"] = str(ex)
            logger.error("CREATE ERR :: %s" % str(ex))
            traceback.print_exc()

        return res

    def fetch_all() -> List[AdminResult]:
        res = Role.all()
        all_data = [x.as_dict() for x in res]
        # print("serialized", all_data)
        # check_data = all_vehicles = [{"vehicle": x.vehicle} for x in vehicle_sum]

        return all_data


    def fetch_by_id_min(id:str) -> AdminResult:
        res = Admin.where('id', '=', id) \
                .get(["first_name", "last_name", "other_names", "sex", "phone", "email", "created_at",]) \
                .first()

        return res

    def fetch_by_email(email:str) -> AdminResult:
        res = Admin.by_email(email) \
            .with_("role") \
            .first()
        #== SELECT `username`, `administrator` as is_admin FROM `users` WHERE `active` = 1
        # res = Admin.where("active", 1).get(["username", "administrator as is_admin"])
        return res


    def fetch_by_phone(phone:str) -> AdminResult:
        res = Admin.by_phone(phone)
        # all_data = [x.as_dict() for x in res]
        # print("serialized", all_data)
        # check_data = all_vehicles = [{"vehicle": x.vehicle} for x in vehicle_sum]
        return res


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

# from schemas.Auth import InstCreate, InstResult
# from models.Institution import Institution
# class InstRepo:

#     async def create(inst: InstCreate) -> InstResult:
#         res = {
#             "errors": {},
#             "data": None
#         }

#         try:
#             db_item= Institution()
#             db_item.id= str(uuid.uuid4())
#             db_item.name= inst.name
#             db_item.phone_no= inst.phone_no
#             db_item.description= inst.description
#             db_item.email= inst.email
#             db_item.address= inst.address
#             db_item.save()
#             res['data'] = db_item
#         except Exception as ex:
#             if 'unique constraint' in str(ex):
#                 logger.error("Institution %s already exists" % inst.name)
#                 res['errors']["unique_constraint"] = str(ex)
#             logger.error(str(ex))

#         return res


#     def fetch_all() -> List[InstResult]:
#         res = Institution.all()
#         all_data = [x.as_dict() for x in res]

#         return all_data


#     def find_by_id(id:str) -> InstResult:
#         res = Institution.where('id', id).get()
#         all_data = [x.as_dict() for x in res]


#     def find_by_name(name:str) -> InstResult:
#         res = Institution.where('name', name).get(["id", "name", "description", "phone_no", "address"])
#         all_data = [x.as_dict() for x in res]

#         return all_data


#     def update1(id:str, data:RoleCreate) -> RoleResult:
#         res = Role.find(id).update(name=data.name, description=data.description)

#         return res


#     def update1(id:str, data:RoleCreate) -> RoleResult:
#         item = Role.find(id)
#         item.name= data.name
#         item.description= data.description

#         item.save()
#         return item