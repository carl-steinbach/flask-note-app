from flask import Blueprint, render_template
from flask import current_app as app


start_bp = Blueprint(
    'start_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@start_bp.route('/')
def start():
    # the landing page for unauthorized users
    return render_template('start.html', title='Note App')
    