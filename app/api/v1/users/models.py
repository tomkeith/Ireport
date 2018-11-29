from flask import jsonify, make_response	

users = []

class UserModels():
	"""docstring for RedFlagsModels"""
	def __init__(self):
		self.db = users
		self.id = len(self.db)+1


	def save_record(self, firstname, lastname, email, username, password):
		payload = {
		"id" : self.id,
		"firstname" : firstname,
		"lastname" : lastname,
		"email" : email,
		"username" : username,
		"password" : password
		}

		self.db.append(payload)

		return self.db
	
	
	def get(self):
		return self.db