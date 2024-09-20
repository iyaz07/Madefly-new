from models import db

class ActivityPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    morning = db.Column(db.String(100))
    evening = db.Column(db.String(100))
    bmi_category = db.Column(db.String(20))
    age_category = db.Column(db.String(20))
    day_of_week = db.Column(db.String(20))