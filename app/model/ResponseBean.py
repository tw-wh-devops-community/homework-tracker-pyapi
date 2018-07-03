from flask import Response


class ResponseBean(Response):
    def __init__(self, return_code, return_msg, response=None):
        self.return_code = return_code
        self.return_msg = return_msg
        self.response = response
