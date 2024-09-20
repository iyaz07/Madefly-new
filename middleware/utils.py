def calculate_bmi(inches, pounds):
    bmi = (pounds * 703) / (inches ** 2)
    return round(bmi, 2)  # Round to 2 decimal places



def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'


def convert_feet_to_inches(height):
    try:
        # Check if height contains both feet and inches
        if "'" in height:
            feet, inches = height.split("'")
            inches = inches.replace('ft', '').strip()  # Clean up any 'ft' or spaces
            feet = int(feet)
            inches = int(inches) if inches else 0
        else:
            # If only feet are provided without inches
            feet = int(height.replace('ft', '').strip())
            inches = 0
        
        return feet * 12 + inches

    except ValueError as e:
        print(f"Error converting height: {e}")
        raise



def kg_to_lbs(weight):
    pounds = float(weight) * 2.20462
    return pounds


def age_group(age):
    age = int(age)
    if age < 50:
        return 'Adult'
    else:
        return 'Senior'
