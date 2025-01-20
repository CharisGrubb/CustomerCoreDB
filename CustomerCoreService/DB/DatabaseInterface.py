
from CustomerCoreService.DB.setup_db import db_setup
import sqlite3
import os


#Parent database connection
class Internal_DB:
    def __init__(self):
        if os.path.exists("CustomerCoreService\DB\CustomerCoreDB.db"):
            self.conn = sqlite3.connect("CustomerCoreService\DB\CustomerCoreDB.db")
        else:
            print("NO INTERNAL DB", os.getcwd())
            db_setup.create_db()
            db_setup.update_db()
    def get_configuration(self, config_name):
        
        return [{}]
    
    def add_configuration(self, config_name, value):
        pass

    def update_configuration(self, config_name, new_value):
        pass
        
    def __convert_results_to_json(self, results,headers:list):
        results_json=[]
        for r in results:
            row_json={}
            for col in range(len(r)):
                row_json[headers[col]]=r[col]
            results_json.append(row_json)
        return results_json