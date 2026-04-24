import bcrypt

def generate_passwd_hash(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(pwd_bytes, salt)
    return hash.decode('utf-8')

def verify_password(password: str, hash: str) -> bool:
    pwd_bytes = password.encode('utf-8')
    hash_bytes = hash.encode('utf-8')
    return bcrypt.checkpw(pwd_bytes, hash_bytes)

