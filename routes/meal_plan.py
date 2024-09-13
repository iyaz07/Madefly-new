from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from models import db, MealPlan

meal_plan_bp = Blueprint('meal_plan', __name__)

@meal_plan_bp.route('/admin/create-meal-plan', methods=['GET', 'POST'])
def create_meal_plan():
    if request.method == 'POST':
        breakfast = request.form.get('breakfast')
        lunch = request.form.get('lunch')
        dinner = request.form.get('dinner')
        region = request.form.get('region')
        bmi_category = request.form.get('bmi_category')
        day_of_week = request.form.get('day_of_week')

        # Validation checks
        if not (breakfast and lunch and dinner and region and bmi_category and day_of_week):
            flash("All fields are required.", "danger")
            return redirect(url_for('meal_plan.create_meal_plan'))

        # Create a new MealPlan instance
        meal_plan = MealPlan(
            breakfast=breakfast,
            lunch=lunch,
            dinner=dinner,
            region=region,
            bmi_category=bmi_category,
            day_of_week=day_of_week
        )

        # Add and commit the new meal plan to the database
        db.session.add(meal_plan)
        db.session.commit()

        flash(f"Meal plan for {day_of_week} created successfully!", "success")
        return redirect(url_for('meal_plan.create_meal_plan'))

    return render_template('create_meal_plan.html')
