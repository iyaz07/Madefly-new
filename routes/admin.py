from flask import Flask, render_template, Blueprint

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin')
def admin_page():
    return render_template('admin.html')
