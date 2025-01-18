from DB.DatabaseInterface import Internal_DB
from DB.IOHelper import IOValidation, Ryptor




class DataHandler:
    
    def __init__(self):
        self.internal_db = Internal_DB()
        external_dbs_configs = self.internal_db.get_configuration('External DB')
        self.external_dbs = []
        for ex_db in external_dbs_configs:
            #Set up each external db and append to list
            pass
    #Getters
    def get_user(self):
        pass

    def get_all_users(self):
        pass

    def get_customer(self):
        pass

    def get_customer_orders(self):
        pass





    ### Modifiers 
    def add_user(self):
        pass

    def add_customer(self):
        pass

    def add_customer_order(self):
        pass

    def update_user(self):
        pass
    
    def update_customer(self):
        pass

    def delete_user(self):
        pass

    def delete_customer(self):
        pass



    