import json

from flask import request, abort, g
from flask_restful import Resource

class hello(Resource):
    def get(self):
        return {"message":"hello"}, 200

class scheduler(Resource):
    def get(self):
        # TODO: get the current time to display
        pass
    
    def put(self):
        # TODO: start or stop scheduler
        pass

class heartRate(Resource):
    def get(self):
        # TODO: get current heartrate
        pass

class heartRateDataset(Resource):
    def get(self):
        # TODO: get all the heart rate data in the database
        pass

