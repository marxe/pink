from passlib.context import CryptContext
from passlib.hash import oracle10
class encrypt:
    def context():
        return CryptContext(
            schemes=["pbkdf2_sha256"],  # scheme type of cryption
            default="pbkdf2_sha256",  # default type of cryption
            pbkdf2_sha256__default_rounds=30000
            # A round is a part of the encryption algorithm that runs many times in order to reduce "crackability"
        )
    def crypt(password):
        crypt = encrypt.context()
        return crypt.encrypt(password)
    def check(password, hashed):
        crypt = encrypt.context()
        return crypt.verify(password, hashed)
    def hash(password, user):
        return oracle10.hash(password, user)
    def verify(password, hash, user):
        return oracle10.verify(password, hash, user)