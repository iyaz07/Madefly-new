from flask import Flask, Blueprint, render_template

comefly_bp = Blueprint('comefly', __name__)


@comefly_bp.route('/comefly',  methods=['GET', 'POST'])
def come_fly(): 
    return render_template('comefly.html')