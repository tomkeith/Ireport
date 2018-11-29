from flask import Flask, Blueprint
from flask_restful import Api, Resource

#local imports
from .api.v1 import api_version_one

def create_app():
	app = Flask(__name__)
	app.register_blueprint(api_version_one)
	return app
	