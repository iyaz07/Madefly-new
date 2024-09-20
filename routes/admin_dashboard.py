from flask import Blueprint, render_template
from models.mealplan import MealPlan
from models.activityplan import ActivityPlan

admin_dashboard_bp = Blueprint('adminDashboard', __name__)

@admin_dashboard_bp.route('/dashboard')
def admin_dashboard():
    meal_plans = MealPlan.query.all()
    activity_plans = ActivityPlan.query.all()
    print(activity_plans)
    print(meal_plans)
    return render_template('dashboard.html', meal_plans=meal_plans, activity_plans=activity_plans)