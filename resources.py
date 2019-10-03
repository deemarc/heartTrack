import json, sys

from flask import request, abort, g
from flask_restful import Resource
from general_tool import global_genDict
from general_tool import db
from models import HeartData
class hello(Resource):
    def get(self):
        return {"App name":"BBB Heart Track",
                "cmd":
                    {
                        "close":"close the app",
                        "myWatch":"check watch timer",
                        "hr":"get current heart rate",
                        "myWatch/<cmd>":{
                            "start":"start watch and save heart rate log",
                            "stop":"stop the watch"
                        },
                        "hrs":"get all heart rate log"
                    }
                }, 200
class close_app(Resource):
    def get(self):
        sys.exit()
        # it won't return
        return {"counter":counter}
class myWatch(Resource):
    def get(self):
        counter = global_genDict['myWatch'].counter
        return {"counter":counter}
class myWatchCmd(Resource):
    def get(self,cmd):
        if cmd == 'start':
            global_genDict['myWatch'].start()
            cmd = 'myWatch start running'
        elif cmd == 'stop':
            global_genDict['myWatch'].stop()
            cmd = 'myWatch is stopping'
        else:
            return {'message':'myWatch cannot understand the command'},405
        return {'message':cmd}, 200

class heartRate(Resource):
    def get(self):
        curBPM = global_genDict['myWatch'].heartrateNow()
        return {"curBPM":curBPM}

class heartRateDataset(Resource):
    def get(self):
        heart_list = []
        heart_datas = db.session.query(HeartData)
        for heart_data in heart_datas:
            heart_detail={
                'id':heart_data.id,
                'cur_bpm':heart_data.cur_bpm,
                'curTime':str(heart_data.curTime),
                'dataset':heart_data.dataset
            }
            heart_list.append(heart_detail)
        # TODO: get all the heart rate data in the database
        return heart_list, 200

