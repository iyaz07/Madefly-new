from models import db

class MealPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breakfast = db.Column(db.String(200))
    lunch = db.Column(db.String(200))
    dinner = db.Column(db.String(200))
    region = db.Column(db.String(20))
    bmi_category = db.Column(db.String(50))
    day_of_week = db.Column(db.String(20))
