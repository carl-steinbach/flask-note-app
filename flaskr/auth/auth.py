"""The authorization logic and routes"""
from flask import Blueprint, render_template, flash, redirect, url_for
from flask import current_app as app
from flask_login import current_user, login_user, logout_user, login_required

from flaskr import db, login_manager
from flaskr.forms import LoginForm, RegistrationForm
from flaskr.models import User


auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """the login page"""
    form = LoginForm()
    if form.validate_on_submit():
        # check credentials and log the user in
        result = db.session.execute(db.select(User)
                    	               .where(User.email==form.email.data)
                                      ).first()
        if result is not None:
            user = result[0]
            if user.password == form.password.data:
                login_user(user)
                flash('logged in')
                # redirect to the users homepage
                return redirect(url_for('home_bp.home'))
            else:
                flash('incorrect password')

        else:
            flash('email is not registered')

    return render_template('login.html', title='Login', form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """registering new users"""
    form = RegistrationForm()
    if (form.validate_on_submit()):
        # check already registered
        result = db.session.execute(db.select(User)
                    	            .where(User.email==form.email.data))
        if result.first() is not None:
            flash('this email is already registered')
        else:
            new_user = User(name=form.name.data, 
                            email=form.email.data, 
                            password=form.password.data
                            )
            db.session.add(new_user)
            db.session.commit()
            flash('account created', 'message')
            return redirect(url_for('auth_bp.login'))

    return render_template('register.html', title='Register', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    """Log out the current user and redirect to landing page"""
    logout_user()
    flash('logged out')
    return redirect(url_for('start_bp.start'))

def login_debug():
    if current_user is not None:
        debug_str = "user.is_active={}, user.is_authenticated={}, user.is_anonymous={}".format(
                        current_user.is_active,
                        current_user.is_authenticated,
                        current_user.is_anonymous
                    )
    else:
        debug_str = "not logged in"
    flash(debug_str)

