from DB.DatabaseHandler import DataHandler
from datetime import datetime


class Logger:

    def __init__(self, log_name, log_type):
        self.log_name = log_name
        self.log_type = log_type
        self.DB = DataHandler()

    def log_to_database(self, log_source, log_level, message, time_of_log=datetime.now(), user = None):
        print(time_of_log)
        self.DB.add_log(self.log_name, self.log_type, log_source, log_level, message, time_of_log, user)
    
    def add_log_to_queue(cls):
        pass

    def push_queued_logs(cls):
        pass


