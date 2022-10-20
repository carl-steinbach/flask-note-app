from flask import Blueprint, flash, render_template
from flask import current_app as app
from flask_login import current_user
from flaskr.models import User

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/home')
def home():
    # the homepage of a user displaying his notes
    user = current_user
    flash(user.name)
    return render_template('home.html', title='Home')
    