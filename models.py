from general_tool import db

class HeartData(db.Model):
    """ heart rate data table """
    __tablename__ = "HeartData"
    id = db.Column(db.Integer, db.Sequence('data_id'), primary_key=True)
    cur_bpm = db.Column(db.Integer)
    curTime = db.Column(db.TIMESTAMP)
    dataset = db.Column(db.Integer)