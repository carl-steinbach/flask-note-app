from flask import Blueprint, flash, render_template, url_for, redirect
from flask import current_app as app
from flask_login import current_user, login_required, logout_user
from flaskr.models import User
from flaskr import db


home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@home_bp.route('/home')
@login_required
def home():
    """The user home page displaying created notes"""
    return render_template('home.html', title='Home')
