from fastapi import HTTPException
from DB.DatabaseInterface import Internal_DB
from Logging.Logger import Logger
import bcrypt 


class Authentication_Authorization:
    def __init__(self):
        self.log = Logger('AUTH')

    def authenticate_user(self, username:str, password:str):
        if username is None or password is None:
            raise HTTPException(status_code=401,detail="Incorrect username or password.", headers={"WWWAuthenticate":"Basic"})
        if not Auth_DB.is_valid_user(username):
            raise HTTPException(status_code=401,detail="Incorrect username or password.", headers={"WWWAuthenticate":"Basic"})
        user_authenticated = False


        return user_authenticated
   
   
    #central point for hashing, allowing updates 
    @staticmethod 
    def hash_data(data_to_hash:str):
        try:
            salty = bcrypt.gensalt()
            hashed_data = bcrypt.hashpw(data_to_hash.encode('utf-8'), salt=salty)
            return hashed_data
        except:
            return None




class Auth_DB(Internal_DB):
    
    @classmethod
    def is_valid_user(cls, username):
        return True
    
    @classmethod 
    def get_user_pw_hash(cls, username):
        pass

