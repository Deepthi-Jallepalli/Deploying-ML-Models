from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Welcome(Resource):
    def get(self):
        return {'about':'Welcome to Flask RESTFul'}
    
    def post(self):
        req_json = request.get_json()
        return {'requested json':req_json},201

api.add_resource(Welcome,'/')

if __name__== '__main__':
    app.run(debug = True)