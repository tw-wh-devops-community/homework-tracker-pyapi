import json
import os

from flask import Flask, request
from flask_cors import CORS

from app.util import HttpUtils as httputils
# from app.service import WxchatService as wxservice
from app.util import WxchatUtils as wxutils
from app.model.MyResponse import MyResponse
# from app.util.HttpUtils import allow_cross_domain


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, supports_credentials=True)
    app.response_class = MyResponse
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # @allow_cross_domain
    @app.route('/pyapi/createAssignment', methods=['POST'])
    def create_assignment_notify():
        j_data = json.loads(request.data)
        print(j_data)
        interview_nick_name = j_data['interviewwxId']
        send_message = httputils.create_assignment_message(j_data)
        return wxutils.send_message(interview_nick_name, send_message)

    return app