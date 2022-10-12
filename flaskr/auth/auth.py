from flask import Blueprint, render_template, flash, redirect, url_for
from flask import current_app as app
from flaskr.forms import LoginForm, RegistrationForm

auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # the login page
    form = LoginForm()
    if form.validate_on_submit():
        flash('now logged in', 'message')
        return redirect(url_for('home_bp.home'))

    return render_template('login.html', title='Login', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # the register page
    form = RegistrationForm()
    if (form.validate_on_submit()):
        flash('now logged in', 'message')
        return redirect(url_for('home_bp.home'))

    return render_template('register.html', title='Register', form=form)
