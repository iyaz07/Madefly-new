# user.py
from models import db
from datetime import datetime
from models.mealplan import MealPlan

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    age = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    bmi = db.Column(db.Integer, nullable=False)
    bmi_category = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'{self.username}, {self.age}'