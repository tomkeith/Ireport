from ... import create_app
import unittest
import json


app = create_app()

class TestUsers(unittest.TestCase):

	def setUp(self):
		app.testing= True
		self.app = app.test_client()
		self.data = {
			"firstname": "mwaka",
			"lastname": "tom",
			"email" : "tom@gmail.com",
			"username" : "tomwaka",
			"password" : "123456"
		}
		
	
	def test_user_login(self):
		response = self.app.get('/api/v1/users')
		self.assertEqual(response.status_code, 200)

	def test_user_registeration(self):
		response = self.app.post('/api/v1/users', data=json.dumps(self.data), content_type='application/json')
		self.assertEqual(response.status_code, 201)

		

if __name__ == '__main__':
	unittest.main()

		


		
