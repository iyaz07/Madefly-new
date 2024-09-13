from flask import Flask, Blueprint, render_template

about_bp = Blueprint('aboutUs', __name__)


@about_bp.route('/about_us')
def about_us():
    return render_template('about.html')