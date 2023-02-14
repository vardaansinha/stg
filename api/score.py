from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.scores import test

score_api = Blueprint('score_api', __name__,
                   url_prefix='/api/scores')


# todo: BE review, observe if API handles error conditions (ie duplicate user id)
#Observe, UI contains inputs that are validated for garbage, data cleaned (ie validate DOB or Password)

 #API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(score_api)

class ScoreAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            score = body.get('score')
            if score is None:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            uid = body.get('uid')
            if uid is None:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            

            ''' #1: Key code block, setup USER OBJECT '''
            uo = test(score=score, 
                      uid=uid)
            
            ''' Additional garbage error checking '''
            # set password if provided

            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {score}, either a format error or User ID {uid} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            users = test.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')