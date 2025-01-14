
CREATE TABLE IF NOT EXISTS Users(
    user_id text not null PRIMARY KEY--UUID
    ,username text NOT NULL
    ,user_pw text NOT NULL -- System to use Salt, hashing, and encryption  before store. SQLite does not support encryption on specific table or columns
    ,access_level INT NOT NULL DEFAULT 0 --CRUD operations Binary/bitwise map. READ=1, CREATE=2,UPDATE=4,DELETE=8 
    ,create_date datetime default CURRENT_TIMESTAMP
    ,CHECK(typeof("user_id") = "text" and length("user_id" <=50)) -- Check to control the length of the uuid for data integrity. UUIDs currently are about 36 characters. Allowing extra space for newer uuid types(Security scalability)
  );



CREATE TABLE IF NOT EXISTS Customers(
    customer_id text not null PRIMARY KEY--UUID
    ,customer_f_name text not null
    ,customer_l_name text not null
    ,customer_m_name text 
    ,create_date datetime default CURRENT_TIMESTAMP
    ,email_address text not null UNIQUE --Add check on app side to ensure correct formate
    ,phone_number text not null 
    ,CHECK(typeof("customer_id") = "text" and length("customer_id" <=50)) -- Check to control the length of the uuid for data integrity. UUIDs currently are about 36 characters. Allowing extra space for newer uuid types(Security scalability)
    
  );

CREATE TABLE IF NOT EXISTS logs(
    log_id INTEGER PRIMARY KEY
    ,user_id text REFERENCES Users(User_ID)
    ,log_note text
    ,log_level text --ERROR, INFO, ALERT, etc
    ,log_type text -- System Connections, Authorization/Authentication, Database Query....
    ,log_source text -- add_customer....remove_customer...
    ,log_name text -- Endpoints-Users, InternalDb, etc
    ,create_date datetime --Timestamp of action occurred
);


PRAGMA User_version = 1;