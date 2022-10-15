from flask import Blueprint, render_template
from flask import current_app as app

index_bp = Blueprint(
    'index_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@index_bp.route('/')
def index():
    # the homepage of a user displaying his notes
    return render_template('index.html', title='Note App')
    