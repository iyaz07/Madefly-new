from flask import Blueprint, render_template, request
from sqlalchemy.exc import IntegrityError
from models import db, User
from middleware.utils import *

fly_status_bp = Blueprint('flyStatus', __name__)

@fly_status_bp.route('/status', methods=['POST'])
def fly_status():
    try:
        # Extract form data
        name = request.form['name']
        age = age_group(request.form['age'])
        height = request.form['height']
        weight = request.form['weight']
        region = request.form['region']

        # Calculate BMI and categorize it
        bmi = calculate_bmi(convert_feet_to_inches(height), kg_to_lbs(weight))
        bmi_category = get_bmi_category(bmi)

        # Create a new user and save to the database
        user = User(username=name, age=age, region=region, bmi=bmi, bmi_category=bmi_category)
        db.session.add(user)
        db.session.commit()

        return render_template('status.html', name=name, bmi=bmi, category=bmi_category)

    except IntegrityError:
        db.session.rollback()
        error_message = f"Username '{name}' already exists. Please choose a different username."
        return render_template('comefly.html', error_statement=error_message, name=name, age=age, height=height, weight=weight, region=region)

    except KeyError:
        error_statement = 'All Form Fields Required'
        return render_template('status.html', error_statement=error_statement, name=request.form.get('name', ''), age=request.form.get('age', ''), height=request.form.get('height', ''), weight=request.form.get('weight', ''), region=request.form.get('region', ''))
