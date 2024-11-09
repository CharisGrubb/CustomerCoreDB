
import sqlite3
import os

#Parent database connection
class Internal_DB:
    def __init__(self):
        if os.path.exists("CustomerCoreService/Database/internal_sensor_database.db"):
            self.conn = sqlite3.connect("CustomerCoreService/Database/internal_sensor_database.db")
        else:
            raise Exception("NO INTERNAL DB", os.getcwd())
        
    def __convert_results_to_json(self, results,headers:list):
        results_json=[]
        for r in results:
            row_json={}
            for col in range(len(r)):
                row_json[headers[col]]=r[col]
            results_json.append(row_json)
        return results_json