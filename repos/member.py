from schemas.musiga.Member import MemberCreate, MemberResult
from models.UserRole import Role
from models.MusigaMember import MusigaMember
import uuid, logging
from typing import List
import traceback


logger = logging.getLogger(__name__)


class MemberRepo:

    # async def create(data: MemberCreate, password:str = None):
    async def create(data: MemberCreate):
        res = { "errors": {}, "data": None }

        try:
            db_item= MusigaMember()
            db_item.id= str(uuid.uuid4())
            db_item.surname= data.surname
            db_item.first_name= data.first_name
            db_item.other_names= data.other_names
            db_item.stage_name= data.stage_name
            db_item.place_of_birth= data.place_of_birth
            db_item.sex= data.sex
            db_item.dob= data.dob
            db_item.contact_no= data.contact_no
            db_item.email= data.email
            db_item.hometown= data.hometown
            db_item.home_region= data.home_region
            db_item.languages_spoken= data.languages_spoken
            db_item.marital_status= data.marital_status
            db_item.member_of_group= data.member_of_group
            db_item.member_type= data.member_type
            db_item.member_id= data.member_id
            db_item.active_status= data.active_status
            db_item.reason= data.reason
            
            db_item.title = data.title
            db_item.country_of_birth = data.country_of_birth
            db_item.citizenship = data.citizenship
            db_item.nhis_no = data.nhis_no
            db_item.ghana_card_no = data.ghana_card_no
            db_item.passport_no = data.passport_no
            db_item.passport_country = data.passport_country
            db_item.passport_expiry_date = data.passport_expiry_date
            db_item.passport_place_of_issue = data.passport_place_of_issue

            db_item.website= data.website
            db_item.music_role= ",".join(map(str, data.music_role))
            db_item.music_role_other= data.music_role_other
            # db_item.passport_image= data.passport_image
            db_item.group_name= data.group_name
            db_item.is_ensemble= data.is_ensemble
            db_item.postal_addr= data.postal_addr
            db_item.residential_addr= data.residential_addr
            db_item.affiliated_musical_assocs= data.affiliated_musical_assocs

            if data.created_by:
                db_item.created_by= str(data.created_by)
            db_item.image_url= data.image_url
            db_item.join_date= data.join_date
            db_item.first_release_date= data.first_release_date
            db_item.last_release_date= data.last_release_date
            db_item.spouse_name= data.spouse_name
            
            db_item.genre= ",".join(map(str, data.genre)) 
            db_item.genre_other= data.genre_other
            db_item.instrument= ",".join(map(str, data.instrument))
            db_item.instrument_other= data.instrument_other
            db_item.has_recorded_songs= data.has_recorded_songs
            db_item.is_member_of_ghamro= data.is_member_of_ghamro
            db_item.is_part_of_other_org= data.is_part_of_other_org
            db_item.no_of_children= data.no_of_children

            db_item.instagram_url= data.instagram_url
            db_item.snapchat_url= data.snapchat_url
            db_item.facebook_url= data.facebook_url
            db_item.tiktok_url= data.tiktok_url
            db_item.youtube_url= data.youtube_url
            db_item.gmx_url= data.gmx_url
            db_item.spotify_url= data.spotify_url
            db_item.audiomack_url= data.audiomack_url
            db_item.boomplay_url= data.boomplay_url
            
            db_item.x_url= data.x_url
            if data.password and data.password != '':
                db_item.password = data.password
            
            db_item.save()            
            res['data'] = db_item.serialize()
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Member %s already exists" % data.first_name+' | '+data.stage_name+' | '+data.email)
                res['errors']["unique_constraint"] = str(ex)
            elif 'violates' in str(ex):
                res['errors']["other"] = str(ex)
            else:
                res['errors']["other"] = str(ex)

            logger.error("ERR DB")
            logger.error(str(ex))

        return res


    def fetch_all_active() -> List[MemberResult]:
        res = MusigaMember.where('active_status', 'active').get([
            "id", "surname", "first_name", "other_names", "stage_name", "email", "member_id", "member_type", 
            "sex", "contact_no", 
            "dob", 
            "hometown", "home_region",
            "marital_status", 
            "join_date", "first_release_date", 
            "music_role", "music_role_other",
        ])
        all_data = res.serialize()

        return all_data


    def fetch_with_status(status: str) -> List[MemberResult]:
        res = MusigaMember.where('active_status', status).get([
            "id", "surname", "first_name", "other_names", "stage_name", "email", "member_id", "member_type", 
            "sex", "contact_no", 
            "dob", 
            "hometown", "home_region",
            "marital_status", 
            "reason", 
            "join_date", "first_release_date", 
            "music_role", "music_role_other",
        ])
        all_data = res.serialize()

        return all_data


    def fetch_all_active_by_region(region: str) -> List[MemberResult]:
        res = MusigaMember\
            .where('active_status', 'active')\
            .where('home_region', region)\
            .get([
                "id", "surname", "first_name", "other_names", "stage_name", "email", "member_id", "member_type", 
                "sex", "contact_no", "dob", "hometown", "home_region",
                "marital_status", "join_date", "first_release_date", "music_role", "music_role_other",
            ])
        all_data = res.serialize()

        return all_data


    def fetch_all_active_by_region_name(region: str) -> List[MemberResult]:
        res = MusigaMember\
            .left_join('musiga_regions', 'musiga_regions.id', '=', 'musiga_members.home_region')\
            .where('active_status', 'active')\
            .where_like('musiga_regions.name', f"%{region}%")\
            .get([
                "id", "surname", "first_name", "other_names", "stage_name", "email", "member_id", "member_type", 
                "sex", "contact_no", "dob", "hometown", "home_region", "musiga_regions.name",
                "marital_status", "join_date", "first_release_date", "music_role", "music_role_other",
            ])
        all_data = res.serialize()

        return all_data


    def fetch_all() -> List[MemberResult]:
        res = MusigaMember.all()
        all_data = res.serialize()

        return all_data


    def get_last_member_id() -> MemberResult:
        # res = MusigaMember.order_by("created_at", "asc").first() # does not work
        # res = MusigaMember.last("created_at")
        res = MusigaMember.order_by("created_at", "desc").limit(1) \
                .get(["id", "member_id", "surname", "first_name", "created_at"]).first()
        all_data = None
        if res:
            all_data = res.serialize()
        # all_data = [x.serialize() for x in res]
        # print("all data", all_data)

        return all_data


    def fetch_by_id(id:str) -> MemberResult:
        all_data = {}
        res = MusigaMember\
                .with_("education") \
                .with_("related_contacts") \
                .with_("artistic_profiles") \
                .with_("extra_info") \
                .where("id", id) \
                .get()
        if res:
            all_data = res.serialize()

        return all_data
    

    def fetch_single_by_id(id:str) -> MemberResult:
        data = MemberRepo.fetch_by_id(id)
        if data:
            data = data[0]

        return data


    def fetch_by_email_or_phone_no(email: str, phone_no: str = None) -> List[MemberResult]:
        member = MusigaMember.where('email', email)\
        
        if phone_no != None:
            member.where('contact_no', phone_no)
            
        member.get([
            "id", "surname", "first_name", "other_names", "stage_name", "email", "member_id", "member_type", 
            "sex", "contact_no", "dob", "hometown", "home_region",
            "marital_status", "join_date", "first_release_date", "music_role", "music_role_other",
        ])\
        .first()
        mem_serialized = member.serialize()

        return mem_serialized


    def fetch_by_email_or_phone_no_combo(login_id: str, is_phone_no: bool = False) -> List[MemberResult]:
        member = MusigaMember.where('email', login_id)
        
        if is_phone_no:
            member = MusigaMember.where('contact_no', login_id)
            
        mem_res = member.get([
            "id", "surname", "first_name", "other_names", "stage_name", "email", "member_id", "member_type", 
            "sex", "contact_no", "dob", "hometown", "home_region",
            "marital_status", "join_date", "first_release_date", "music_role", "music_role_other",
        ])\
        .first()
        mem_serialized = mem_res.serialize()

        return mem_serialized


    async def set_member_password(id:str, new_password:str):
        res = {
            "errors": {},
            "data": None
        }

        try:
            db_res = MusigaMember.find(id).update({"password":new_password,})
            res['data'] = db_res.serialize()
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Admin %s password could not be updated" % db_res.first_name+' '+db_res.surname)
                res['errors']["unique_constraint"] = str(ex)
            logger.error("UPDATE ERR :: %s" % str(ex))
            traceback.print_exc()

        return res


    from schemas.musiga.Member import UpdateStatusRequest
    # async def update_active_status(id:str, active_status:str):
    async def update_active_status(id:str, data: UpdateStatusRequest):
        res = { "errors": {}, "data": None }

        try:
            db_res = MusigaMember.find(id).update({"active_status":data.active_status, "reason": data.reason})
            res['data'] = db_res.serialize()
        except Exception as ex:
            msg = "Member with ID: %s active status could not be updated" % id
            res['errors']["msg"] = msg
            res['errors']["other"] = str(ex)
            logger.error("UPDATE ERR :: %s" % str(ex))
            # traceback.print_exc()

        return res


    def fetch_by_id_for_login(login_id: str, is_phone_no: bool = False) -> List[MemberResult]:
        member = MusigaMember.where('email', login_id)
        if is_phone_no:
            member = MusigaMember.where('contact_no', login_id)
            
        mem_res = member.get([
            "id", "surname", "first_name", "other_names", "stage_name", "email", "member_id", "member_type", 
            "sex", "contact_no", "dob", "hometown", "home_region",
            "password", "join_date", "music_role", "music_role_other", "active_status",
        ])\
        .first()
        mem_serialized = mem_res.serialize()

        return mem_serialized
# user = User.find(1)
# # All users phones
# phones = user.phones 
# # All active users phones
# active_phones = user.related("phones").where("active", 1).get()


