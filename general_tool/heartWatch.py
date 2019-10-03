from flask_apscheduler import APScheduler
from sqlalchemy import desc
from general_tool.dbSession import DBSession
import Adafruit_GPIO.I2C as I2C
import datetime
from models import HeartData
class HeartWatch(object):
    def __init__(self, app):
        self.scheduler = APScheduler()
        self.scheduler.init_app(app)
        self.counter = 0
        self.dbUrl = app.config['SQLALCHEMY_DATABASE_URI']
        self.scheduler.add_job("watchTask", self.__task, 
                            trigger="interval",
                            seconds=1)
    def start(self):
        print('start log')
        try:
            self.scheduler.start()
        except Exception as e:
            # self.logger("Error from HeartWatch Start process:{0}".format(str(e)))
            raise e
    def stop(self):
        try:
            self.scheduler.shutdown()
        except Exception as e:
            # self.logger("Error from HeartWatch Stop process:{0}".format(str(e)))
            raise e
    def __task(self):
        self.counter = self.counter + 1
        mySess = DBSession(self.dbUrl)
        with mySess.ManagedSession() as session:
            data = {}
            data['curTime'] = datetime.datetime.now()
            data['cur_bpm'] = self.heartrateNow()
            # dataset = session.query(HeartData).order_by(desc(HeartData.dataset)).first()
            # if dataset:
            #     data['dataset'] = dataset + 1
            # else:
            #     data['dataset'] = 0
            data['dataset'] = 0
            new_heart_data = HeartData(**data)
            session.add(new_heart_data)
    @staticmethod
    def heartrateNow():
        i2c = I2C.Device(0x50,2)
        curBPM = i2c.readS8(0xA0)
        return curBPM
        
