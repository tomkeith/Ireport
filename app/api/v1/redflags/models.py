from flask_restful import Resource
from flask import jsonify, make_response, request
import datetime



redflags = []

class RedFlagsModels():
	"""docstring for RedFlagsModels"""
	def __init__(self):
		self.db = redflags


	def save_record(self, createdBy, location, comment):
		payload = {
		  'id' : len(self.db)+1,
		  'createdOn' : datetime.datetime.now().strftime('%I:%M%p %B %d, %Y'),  
		  'createdBy' : createdBy, 
		  'type' : "redflag",       
		  'location' : location,   
		  'status' : "draft",     
		  'Images' : "images", 
		  'Videos' : "videos",
		  'comment' : comment
		
		}

		self.db.append(payload)

		return self.db
	
	
	def get_all(self):
		return self.db

	def edit_location(self, num):
		for redflag in self.db:
			if redflag['id'] == int(num):
				if redflag ['status'] == 'draft':
					redflag.update(request.get_json())
					return{
						'status':200,
						'data':[{
							'id': num,
							'message':'updated redflag location'
						}]
					}
				elif redflag['status'] == 'under investigation':
					return{
						'status':404,
						'message': 'redflag under investigation'
					}
				elif redflag['status'] == 'Resolved':
					return{
						'status':404,
						'message': 'redflag Resolved'
					}
				elif redflag['status'] == 'Rejected':
					return{
						'status':404,
						'message': 'redflag Rejected'
					}

	def edit_comment(self, num):
		for redflag in self.db:
			if redflag['id'] == int(num):
				if redflag ['status'] == 'draft':
					redflag.update(request.get_json())
					return{
						'status':200,
						'data':[{
							'id': num,
							'message':'updated redflag comment'
						}]
					}
				elif redflag['status'] == 'under investigation':
					return{
						'status':404,
						'message': 'redflag under investigation'
					}
				elif redflag['status'] == 'Resolved':
					return{
						'status':404,
						'message': 'redflag Resolved'
					}
				elif redflag['status'] == 'Rejected':
					return{
						'status':404,
						'message': 'redflag Rejected'
					}

		
		
	def get_one(self, num):
		for redflag in self.db:
			if redflag['id'] == num:
				return redflag
			else:
				return "No content found"

	

	def destroy(self, num):
		for redflag in redflags:
			if redflag['id'] == num:
				redflags.pop(num - 1)
				return "Deleted successfully"
			else:
				return "No content found"

	
		
