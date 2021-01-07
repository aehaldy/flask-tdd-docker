# src/__init__.py


from flask import Flask, jsonify
from flask_restx import Resource, Api
import os
import sys


# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong along world!'
        }


api.add_resource(Ping, '/ping')
