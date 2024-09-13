from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

from models.activityplan import ActivityPlan
from models.mealplan import MealPlan
from models.user import User
