from cryptography.fernet import Fernet 
import base64
import os
import re


class IOValidation:
    

    @staticmethod
    def validate_user_name(username:str):
        #Check length
        if len(username)>100:
            raise Exception("Username length exceeds 100 character allowance.")

        #Check for invalid characters; whitelist of only lower and upper case alphabet, numbers, and underscore
        check_for_disallowed_characters = re.search("[^A-Za-z0-9_]",username)
        if check_for_disallowed_characters:
            raise Exception("Invalid character [" + check_for_disallowed_characters.group()+ "] detected in Username: {username}")
        

        return username

    @staticmethod
    def validate_user_pw(pw:str):
        #Check length between min and max (min 12 characters)
        if len(pw) < 12:
            raise Exception("Password length requirement not met. Need at least 12 characters.")
        if len(pw)>50:
             raise Exception("Password length too long. Character limit is 50.")

        #REGEX Check for unwanted characters 
        check_for_disallowed_characters = re.search("[^A-Za-z0-9_!@#$%^&*.'`]",pw)
        if check_for_disallowed_characters:
            raise Exception("Invalid character [" + check_for_disallowed_characters.group()+ "] detected in Password.")
        
        #Check for min needed character variety (capital, lower, number, special character)
        if not re.search(r"[a-z]", pw):
            raise Exception("Password requires at least one lower case")
        if not re.search(r"[A-Z]", pw):
            raise Exception("Password requires at least one upper case")
        if not re.search(r"[0-9]", pw):
            raise Exception("Password requires at least one mumber")
        if not re.search(r"[!@#$%&*+=_-]", pw):
            raise Exception("Password requires at least one of the following special characters: !, @, #, $, %, &, *, +, =, _, or -")
        

        #return the password back if it successfully makes it past all checks
        return pw

#Helper for Encryption and Decryption
class Ryptor:
    @staticmethod
    def encrypt(data_to_encrypt:str):
      
        
        key = os.environ.get('CustomerCore_ENC_KEY')
        f = Fernet(key)
        token = f.encrypt(data_to_encrypt.encode('utf-8'))

        return token

     

    
    @staticmethod
    def decrypt(data_to_decrypt:str):
        
        
        key = os.environ.get('CustomerCore_ENC_KEY')
        f = Fernet(key)
        token = f.decrypt(data_to_decrypt.encode('utf-8'))

        return token

    #Called on set up, to create/load key
    @staticmethod 
    def load_encryption_key():
        try:
            print('Load Encryption key')
            key = Fernet.generate_key()

            os.environ["CustomerCore_ENC_KEY"] = base64.b64encode(key).decode('utf-8') #Environment variables have to be string, encode and convert to string

            return True
        except:
            return False

    @staticmethod 
    def check_for_encryption_key():
        try:

            key = base64.b64decode(os.environ["CustomerCore_ENC_KEY"]) #Key is stored in the environment variable as a base64 utf-8 encoded string. Decode into bytes for Fernet
            f = Fernet(key)#Should error for an invalid key
            return True
        except:
            return False