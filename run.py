from app import create_app
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource



app = create_app()

if __name__ == '__main__':
	app.run(debug=True)
