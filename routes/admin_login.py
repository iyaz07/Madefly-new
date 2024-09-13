from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash

admin_login_bp = Blueprint('adminLogin', __name__)

# Predefined admin credentials
admin_email = 'admin@gmail.com'
admin_password_hash = generate_password_hash('password')  # Use hashed password

@admin_login_bp.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the provided credentials match the predefined admin credentials
        if email == admin_email and check_password_hash(admin_password_hash, password):
            # Simulating admin user login (no database user)
            admin_user = {
                'email': admin_email,
                'is_admin': True
            }
            return redirect(url_for('adminDashboard.admin_dashboard'))
        else:
            flash('Invalid email or password. Please try again.')

    return render_template('admin_login.html')
