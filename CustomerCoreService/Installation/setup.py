import os
import sqlite3
import tkinter
import tkinter.messagebox
import tkinter.simpledialog 
import traceback

from Auth.AuthHandler import Authentication_Authorization
from Database.DatabaseInterface import Internal_DB, IOHelper



##### Connect to database (create new database if it doesn't exist) 

conn = sqlite3.connect("CustomerCoreService/Database/internal_sensor_database.db")

cursor = conn.cursor()



#GET CURRENT USER VERSION 
cursor.execute("PRAGMA user_version")
current_user_version = cursor.fetchall()[0][0] #Used to tell which update scripts need ran for the DB

if current_user_version==0:
    #Run initiation and create scripts
    with open('CustomerCoreService/Installation/Database/create_tables.sql') as sql_file: 
        cursor.executescript(sql_file.read()) #Create Tables
        conn.commit() #Commit creation



##Set up encryption key
db = Internal_DB()
if not IOHelper.Ryptor.check_for_encryption_key():
    db._update_encryptions() #Will create new encryption key if it doesn't exist, otherwise, it will rotate the key
elif tkinter.messagebox.askquestion("Rotate Keys?","""Would you like to rotate encryption keys during this update? 
                                        Rotating keys and passwords periodically is part of security hygeine and best practices.""") == 'yes':
    db._update_encryptions() #Will rotate key if it already exists.

#Check for existing admin user that is enabled. 



#Prompt user for the default Username/password internal account:
username = None
pw = None
error_msg=''
while username is None:
    username = tkinter.simpledialog.askstring("Internal Admin Username",error_msg + "What username would you like for the built in administrative account:")
    #Call username validation
    try:
        IOHelper.InputOutputValidation.validate_user_name(username)
    except:
        username = None
        error_msg="Invalid username. Please, try again..."
error_msg=''
while pw is None:    
    try: #### SEE IF TYPING CAN DO THE MASKING DOTS IN THIS...with button for showing password? 
        pw = tkinter.simpledialog.askstring(f"Internal Admin Password",error_msg + """What password would you like for {username}:
                                            \n Password Requirements include at least 1 capital/upper case letter, 1 lower case letter, 1 number, 
                                            and 1 special character [Options: !, @, #, $, %, &, *, +, =, _, or -]""")
        #call password validation
        IOHelper.InputOutputValidation.validate_user_pw(pw)
    except:
        print(traceback.format_exc())
        pw = None
        error_msg = "Invalid password. Please, try again..."


#hash pw
pw_hash = Authentication_Authorization.hash_data(pw)


#store pw in database, creating user
db.add_user(username, 'Internal','Administrator', pw, 'Global Admin')



conn.close() #ALWAYS close your connections ;)
