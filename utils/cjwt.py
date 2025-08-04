from fastapi import Request, HTTPException,status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .exception_handler import ErrorException
import os, logging
import jwt
import time
from hashlib import sha256, md5
import bcrypt
import random
import string
from dotenv import load_dotenv


load_dotenv()
logger = logging.getLogger(__name__)

JWT_SECRET:str=os.getenv('AUTH_SECRET')
JWT_MEMBER_SECRET:str=os.getenv('AUTH_MEMBER_SECRET')
JWT_ALGORITHM:str=os.getenv('AUTH_ALGORITHMS')


def has_token_expired(auth_user_id:str,expires_at:float,token:str):
    try:
        query="""
            query getRecentToken($owner:String){
                expired_access_token(order_by:{created_at:desc},limit:1,where:{owner:{_eq:$owner}}){
                    token
                }
            }
        """
        plain_text=f'{auth_user_id}@{expires_at}'

        variables={
            "owner": str(md5(sha256(plain_text.encode('utf-8')).hexdigest().encode('utf-8')).hexdigest())
        }

        # client = GraphqlClient(endpoint=url, headers=headers)
        # data:dict=client.execute(query=query, variables=variables)
        # print('My Token Data',data)

        # if data.get('data') and data['data']['expired_access_token']:
        #     db_token:str=data['data']['expired_access_token'][0]['token']
        #     return db_token==sha256(token.encode('utf-8')).hexdigest()
        
    except Exception as e:
     print('Token expired exception',str(e))

    return False


def get_password_hash(password: str):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(13)
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    hashed_password = hashed_bytes.decode('utf-8')
    
    return hashed_password


def is_valid_password(password:str, hashed_password):
    verify_pwd = bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    if verify_pwd:
        return True
    return False


def generate_random_passord():
    special_characters = "!@"
    text_length = 8

    # Exclude characters 'o0O1ILl' from the pool of characters
    characters = ''.join(set(string.ascii_letters + string.digits + special_characters) - set('o0O1ILl'))

    random_text = ''.join(random.choice(characters) for _ in range(text_length))
    return random_text


# def decodeJWT(token: str) -> dict:
#     try:
#         decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
#         return decoded_token if decoded_token["exp"] >= time.time() else None
#     except:
#         return {}


# def signJWT(userpayload) -> dict[str, str]:  
#     current_time = int(time.time()) 
#     expiration_time = current_time + 86400
#     payload = {
#         'role':userpayload.get("role_id") or None,
#         "sub": userpayload['id'],
#         "exp": expiration_time,
#         "inst": userpayload['inst'],
#     }

#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
#     response={
#         'token':token,
#         'expires_at':expiration_time
#     }
#     return response


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True) -> None:
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication scheme")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token or expired token")

            return credentials.credentials
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authorization code")


    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = self.decode_jwt(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid


    # def decode_jwt(self, jwtoken: str):
    #     try:
    #         payload = jwt.decode(jwtoken, JWT_SECRET, algorithms=[JWT_ALGORITHM]) 
    #         return payload
    #     except jwt.ExpiredSignatureError:
    #         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Expired token")
    #     except jwt.InvalidTokenError:
    #         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")


    def decode_jwt(self, token: str) -> dict:
        try:
            decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return decoded_token if decoded_token["exp"] >= time.time() else None
        except:
            return {}


    # def signJWT(userpayload) -> dict[str, str]:  
    def sign_jwt(userpayload) -> dict[str, str]:
        current_time = int(time.time()) 
        expiration_time = current_time + 86400
        payload = {
            'role':userpayload.get("role_id") or None,
            "sub": userpayload['id'],
            "exp": expiration_time,
            # "inst": userpayload['inst'],
        }

        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        response={
            'token':token,
            'expires_at':expiration_time
        }
        return response


    def get_role(self, jwtoken: str):
        payload = self.decode_jwt(jwtoken)
        if 'role' in payload:
            query="""
                query MyQuery($role_id:uuid!) {
                roles(where: {id: {_eq: $role_id}}) {
                    name
                }
                    }
                """
            # client = GraphqlClient(endpoint=url, headers=headers)
            # data:dict=client.execute(query=query, variables={
            #     "role_id":payload['role']
            # })
            # if data.get('data') and data['data']['roles']: 
            #     return data['data']['roles'][0]['name']
        return None
    
    def get_user_id(self,jwtoken:str):
        payload = self.decode_jwt(jwtoken)
        if 'sub' in payload:
            return payload['sub']
        else:
            return None


'''
JWT bearer class for authenticating MUSIGA members
'''
class JWTMemberBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True) -> None:
        super(JWTMemberBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTMemberBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid member authentication scheme")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or expired member token")

            return credentials.credentials
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid member authorization code")


    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = self.decode_jwt(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid


    def get_user_id(self,jwtoken:str):
        payload = self.decode_jwt(jwtoken)
        if 'sub' in payload:
            return payload['sub']
        else:
            return None


    def get_role(self, jwtoken: str):
        payload = self.decode_jwt(jwtoken)
        if 'role' in payload:
            query="""
                query MyQuery($role_id:uuid!) {
                roles(where: {id: {_eq: $role_id}}) {
                    name
                }
                    }
                """

        return None


    def sign_jwt(userpayload) -> dict[str, str]:
        current_time = int(time.time()) 
        expiration_time = current_time + 86400
        payload = {
            # 'role':userpayload.get("role_id") or None,
            "sub": userpayload['id'],
            "exp": expiration_time,
        }
        logger.warning(f"CJWT :: {JWT_MEMBER_SECRET}")
        token = jwt.encode(payload, JWT_MEMBER_SECRET, algorithm=JWT_ALGORITHM)
        response={
            'token':token,
            'expires_at':expiration_time
        }
        return response
    
    def decode_jwt(self, jwtoken: str):
        try:
            payload = jwt.decode(jwtoken, JWT_MEMBER_SECRET, algorithms=[JWT_ALGORITHM]) 
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Expired token")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")
