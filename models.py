from db import db

class heart_data(db.Model):
    """ heart rate data table """
    __tablename__ = "heart_data"
    id = db.Column(db.Integer, db.Sequence('data_id'), primary_key=True)
    cur_bpm = db.Column(db.Integer)
    curTime = db.Column(db.Timestamp)
    dataset = db.Column(db.Integer)