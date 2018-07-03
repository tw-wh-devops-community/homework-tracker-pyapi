from flask import Response, jsonify
from app.model.ResponseBean import ResponseBean


class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, ResponseBean):
            response = {
                'returnCode': response.return_code,
                'returnMsg': response.return_msg,
                'response': response.response
            }
            response = jsonify(response)
        elif isinstance(response, (list, dict)):
            response = jsonify(response)
        print(response)
        return super(Response, cls).force_type(response, environ)