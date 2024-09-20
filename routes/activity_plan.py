from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from models import db, ActivityPlan

activity_plan_bp = Blueprint('activity_plan', __name__)

@activity_plan_bp.route('/admin/create-activity-plan', methods=['GET', 'POST'])
def create_activity_plan():
    if request.method == 'POST':
        morning = request.form.get('morning')
        evening = request.form.get('evening')
        age_category = request.form.get('age_category')
        bmi_category = request.form.get('bmi_category')
        day_of_week = request.form.get('day_of_week')

        # Validation checks
        if not (morning and evening and age_category and bmi_category and day_of_week):
            flash("All fields are required.", "danger")
            return redirect(url_for('activity_plan.create_activity_plan'))

        # Create a new ActivityPlan instance
        activity_plan = ActivityPlan(
            morning=morning,
            evening=evening,
            age_category=age_category,
            bmi_category=bmi_category,
            day_of_week=day_of_week
        )

        # Add and commit the new meal plan to the database
        db.session.add(activity_plan)
        db.session.commit()

        flash(f"Activity plan for {day_of_week} created successfully!", "success")
        return redirect(url_for('activity_plan.create_activity_plan'))

    return render_template('create_activity_plan.html')
