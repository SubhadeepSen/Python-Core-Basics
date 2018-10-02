class UserException(Exception):
    def __init__(self, message=""):
        self.message = message;

    def get_message(self):
        return self.message;



try:
    raise UserException("This is a user defined exception");
except UserException as excp:
    print(excp.get_message());
    
