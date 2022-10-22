from flask import Blueprint, flash, url_for, redirect, request, render_template
from flask import current_app as app

from flask_login import current_user, login_required, logout_user

from flaskr.forms import CreateNoteForm
from flaskr.models import User, Note
from flaskr import db


home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@home_bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    """The user home page displaying created notes"""
    form = CreateNoteForm()
    
    if form.validate_on_submit():
        note = Note(title=form.title.data, content=form.content.data, user=current_user.id)
        db.session.add(note)
        db.session.commit()
        
    return render_template('home.html', title='Home', form=form)
