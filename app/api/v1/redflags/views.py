from flask_restful import Resource
from flask import jsonify, make_response, request

from .models import RedFlagsModels



class RedFlags(Resource, RedFlagsModels):
	

	def __init__(self):
		self.db = RedFlagsModels()

	def post(self):
		data=request.get_json()
		createdBy=data['createdBy']
		location=data['location']
		comment = data['comment']

		resp = self.db.save_record(createdBy, location, comment)

		return make_response(jsonify(
			{
			"data" : resp,
			"status" : 201
			}), 201)

	def get(self):
		resp = self.db.get_all()

		return make_response(jsonify(
			{
			"data" : resp,
			"status" : 200
			}), 200)

	def put(self, num):
		resp = self.db.put(num)

		return make_response(jsonify(
			{
			"data" : resp,
			"status" : 200
			}), 200)



		

class RedFlag(Resource, RedFlagsModels):
	"""docstring for RedFlag"""
	def __init__(self):
		self.model = RedFlagsModels()

	def get(self, num):
		resp = self.model.get_one(num)

		return make_response(jsonify(
			{
			"data" : resp,
			"status" : 200
			}), 200)

	def patch(self, num):
		try:
			int(num)
		except ValueError:
			return{
				'status': 404,
				'error': 'Valid id required'
			}
		editlocation = self.model.edit_location(num)
		return editlocation

	def delete(self, num):
		resp = self.model.destroy(num)

		return make_response(jsonify(
			{
			"data" : resp,
			"status" : 204
			}), 204)
		

