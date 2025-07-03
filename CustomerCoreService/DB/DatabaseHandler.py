from DB.DatabaseInterface import DB
from DB import DB_Models
from DB.IOHelper import IOValidation, Ryptor
from sqlalchemy.orm import Session



#TO manage the flow of data to and from internal and external DBs
class DataHandler:
    
    def __init__(self):
        self.internal_db = DB()
        external_dbs_configs = self.internal_db.get_configuration('External DB')
        self.external_dbs = []
        for ex_db in external_dbs_configs:
            self.external_dbs.append(DB(location=ex_db['Connection String']))

    #Getters
    def get_user(self): #User stuff only to iternal
        pass

    def get_all_users(self):
        pass

    def get_customer(self): 
        pass

    def get_customer_orders(self):
        pass

    def get_num_customers(self):
        return 0
    
    def get_num_cust_trend(self):
        pass





    ### Modifiers 
    def add_user(self):
        pass

    def add_customer(self):
        pass

    def add_customer_order(self):
        pass

    def add_log(self):
        with Session(self.internal_db.engine) as sess:
            new_log = DB_Models.Log()
            sess.add(new_log)
            sess.commit()


    def update_user(self):
        pass
    
    def update_customer(self):
        pass

    def delete_user(self):
        pass

    def delete_customer(self):
        pass



    