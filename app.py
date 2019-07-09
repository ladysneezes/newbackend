from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.debug = True

class HelloWorld(Resource):
    def get(self):
        return {"msg": "Hello, Team"}


api.add_resource(HelloWorld, '/')

