from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from model.facts import FactDay

fact_api = Blueprint('fact_api', __name__, url_prefix='/api/fact')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(fact_api)

class factAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            date = body.get('')
            if date is None or len(date) < 2:
                return {'message': f'Date is missing, or is less than 2 characters'}, 210
            
            # look for score, type
            score = body.get('score')
            type = body.get('type')
            #day = body.get('day')
            # validate uid
            #uid = body.get('id')
            #if uid is None or len(uid) < 2:
            #    return {'message': f'ID is missing, or is less than 2 characters'}, 210
            #''' #1: Key code block, setup USER OBJECT '''
            
            uo = FactDay(date=date, fact=fact)
            
            ''' Additional garbage error checking '''
            
            # create nfl news in database
            facts = uo.create()
            # success returns json of nfl news
            if facts:
                return jsonify(facts.read())
            # failure returns error
            return {'message': f'Processed news error'}, 210

    class _Read(Resource):
        def get(self):
            facts = FactDay.query.all()    # read/extract all users from database
            json_ready = [team.read() for date in dates]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
