from flask import Blueprint, render_template
from models import db, MealPlan, User, ActivityPlan

gofly_bp = Blueprint('gofly', __name__)

@gofly_bp.route('/gofly/<name>')
def go_fly(name):
    # Retrieve the user based on the provided name
    user = User.query.filter_by(username=name).first()
    
    # If user not found, return an error message
    if not user:
        return "User not found", 404

    # Retrieve user meal plans and activity plans
    meal_plans = MealPlan.query.filter_by(bmi_category=user.bmi_category, region=user.region).limit(7).all()
    activity_plans = ActivityPlan.query.filter_by(bmi_category=user.bmi_category).limit(7).all()

    # Render the template with the retrieved data
    return render_template('gofly.html', user=user, meal_plans=meal_plans, activity_plans=activity_plans)
