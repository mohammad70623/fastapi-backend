import bcrypt
from datetime import timedelta, datetime
from src.config import config
import jwt
import uuid
import logging

ACCESS_TOKEN_EXPIRY = 3600

def generate_passwd_hash(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(pwd_bytes, salt)
    return hash.decode('utf-8')

def verify_password(password: str, hash: str) -> bool:
    pwd_bytes = password.encode('utf-8')
    hash_bytes = hash.encode('utf-8')
    return bcrypt.checkpw(pwd_bytes, hash_bytes)


def create_access_token(user_data: dict, expiry:timedelta = None,refresh: bool = False):

    payload={}
    payload['user'] = user_data
    payload['exp'] = datetime.now()+ (expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRY))
    payload['jti'] = str(uuid.uuid4())
    payload['refresh'] = refresh
    token = jwt.encode(
        payload=payload,
        key=config.JWT_SECRET,
        algorithm=config.JWT_ALGORITHM
    )  
    return token

def decode_token(token: str)->dict:
    try:
        token_data = jwt.decode(
            jwt=token,
            key=config.JWT_SECRET,
            algorithms=[config.JWT_ALGORITHM]
        )

        return token_data
    
    except jwt.PyJWTError as e:
        logging.exception(e)
        return None
    
