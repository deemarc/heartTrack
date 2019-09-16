from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
# import smbus
# import Adafruit_GPIO.I2C as I2C
from config import Config
from resources import hello
app = Flask(__name__)
api = Api(app)

app_config = Config()
# class heartRate(Resource):
#     def get(self):
#         i2c = I2C.Device(0x50,2)
#         curBPM = i2c.readS8(0xA0)
#         retJson = {"curBPM":curBPM}
#         return retJson

# api.add_resource(heartRate, "/")
api.add_resource(hello,"/hello")
# api.add_resource(addTwoNumber, "/addTwoNumber")
# api.add_resource(sumAll, "/sumAll")
# api.add_resource(isPalindrome, "/isPalindrome")
# api.add_resource(divideTwoNum, "/divideTwoNum")
def create_app():
    app = Flask(__name__, static_url_path='')
    app.config['SQLALCHEMY_DATABASE_URI'] = app_config.environment["connections"]['connection']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)

    from db import db
    db.init_app(app)
    # If you try to perform database operations outside an application context, you will see the following error
    # error message: "No application found. Either work inside a view function or push an application context."
    app.app_context().push()
    return app


if __name__ =="__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8001)