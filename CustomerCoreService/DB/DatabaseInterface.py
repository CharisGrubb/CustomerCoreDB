from DB.DB_Models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker


class DB:
    def __init__(self, location = "sqlite:///DB/customercore.db"):
        self.engine = create_engine(location) 
        # Create the table in the database
        Base.metadata.create_all(self.engine)
        print("Inside the DB creation constructor")
        # Create a session factory
        self.Session = sessionmaker(bind=self.engine)


    def get_configuration(self, config_name):
        
        return []
    
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