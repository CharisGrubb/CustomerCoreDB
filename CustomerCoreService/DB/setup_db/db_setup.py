import os
import sqlite3

##### Connect to database (create new database if it doesn't exist) 
def connect():
    conn = sqlite3.connect("CustomerCoreService\DB\CustomerCoreDB.db")

    cursor = conn.cursor()

    return conn, cursor

def create_db():
    conn,cursor = connect()

    #GET CURRENT USER VERSION 
    cursor.execute("PRAGMA user_version")
    current_user_version = cursor.fetchall()[0][0] #Used to tell which update scripts need ran for the DB
    print(current_user_version)
    if current_user_version==0:
        #Run initiation and create scripts
        with open('C:\Tools\CustomerCoreDB\CustomerCoreService\DB\setup_db\create_tables.sql') as sql_file: 
            cursor.executescript(sql_file.read()) #Create Tables
            conn.commit() #Commit creation

        with open('C:\Tools\CustomerCoreDB\CustomerCoreService\DB\setup_db\create_indexes.sql') as sql_file: 
            cursor.executescript(sql_file.read()) #Create Tables
            conn.commit() #Commit creation
        
        with open('C:\Tools\CustomerCoreDB\CustomerCoreService\DB\setup_db\create_stored_procedures.sql') as sql_file: 
            cursor.executescript(sql_file.read()) #Create Tables
            conn.commit() #Commit creation


def update_db():
    conn,cursor = connect()
    
    update_file_paths = os.listdir('CustomerCoreService\DB\setup_db\updates')
    for file in update_file_paths:
        print(file)

        #Check file update number, if it is greater than users current version...execute.


