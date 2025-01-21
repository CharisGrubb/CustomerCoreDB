from DB.DatabaseInterface import Internal_DB

class Logger:

    def __init__(self, log_name):
        self.log_name = log_name

    def log_to_database(self, log_source, message, time_of_log, user = None):
        pass
    
    def add_log_to_queue(cls):
        pass

    def push_queued_logs(cls):
        pass


class Logger_DB(Internal_DB):
    
    @classmethod 
    def add_log(cls):
        pass