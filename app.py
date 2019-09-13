from flask import Flask
from flask_restful import Api, Resource
# import smbus
import Adafruit_GPIO.I2C as I2C
app = Flask(__name__)
api = Api(app)

class heartRate(Resource):
    def get(self):
        i2c = I2C.Device(0x50,2)
        curBPM = i2c.readS8(0xA0)
        retJson = {"curBPM":curBPM}
        return retJson

api.add_resource(heartRate, "/")
# api.add_resource(addTwoNumber, "/addTwoNumber")
# api.add_resource(sumAll, "/sumAll")
# api.add_resource(isPalindrome, "/isPalindrome")
# api.add_resource(divideTwoNum, "/divideTwoNum")

if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True)