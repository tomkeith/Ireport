from ... import create_app
import unittest
import json


app = create_app()

class TestRedFlags(unittest.TestCase):

	def setUp(self):
		app.testing = True 
		self.app = app.test_client()
		self.data = {
			  "createdBy" : "Tom",
			  "location" : "45E, 24N",
			  "status" : "draft", 
			  "Images" : "image", 
			  "Videos" : "video",
			  "comment" : "whosmatternow"
			}
	
	def test_redflag_get(self):
		response = self.app.get('/api/v1/redflags')
		self.assertEqual(response.status_code, 200)

	def test_redflag_post(self):
		response = self.app.post('/api/v1/redflags', data=json.dumps(self.data), content_type='application/json')
		self.assertEqual(response.status_code, 201)

	def test_redflag_patch(self):
		self.data2 = {
			  "createdBy" : "mwaka",
			  "location" : "45E, 29N",
			  "status" : "draft", 
			  "Images" : "image", 
			  "Videos" : "video",
			  "comment" : "whosmatternow"
			}
		response = self.app.patch('/api/v1/redflag/1', data=json.dumps(self.data2), content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_redflag_put(self):
		self.data2 = {
			  "createdBy" : "mwaka",
			  "location" : "45E, 29N",
			  "status" : "draft", 
			  "Images" : "image", 
			  "Videos" : "video",
			  "comment" : "whosmatternow"
			}
		response = self.app.put('/api/v1/redflags/1', data=json.dumps(self.data2), content_type='application/json')
		self.assertEqual(response.status_code, 200)
		



if __name__ == '__main__':
	unittest.main()


