class ErrorException(Exception):
    def __init__(self, status_code: str,message:str):
        self.status_code = status_code
        self.message = message