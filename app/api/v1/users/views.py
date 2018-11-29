from flask_restful import Resource
from flask import jsonify, make_response, request

from .models import UserModels
		

class Users(Resource, UserModels):
	

	def __init__(self):
		self.db = UserModels()

	def post(self):
		data=request.get_json()
		firstname=data['firstname']
		lastname=data['lastname']
		email=data['email']
		username=data['username']
		password=data['password']

		resp = self.db.save_record(firstname, lastname, email, username, password)

		return make_response(jsonify(
			{
			"data" : resp,
			"status" : 201
			}), 201)

	def get(self):
		resp = self.db.get()

		return make_response(jsonify(
			{
			"data" : resp,
			"status" : 200
			}), 200)
	