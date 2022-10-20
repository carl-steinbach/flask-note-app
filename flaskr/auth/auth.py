"""The authorization logic and routes"""
from flask import Blueprint, render_template, flash, redirect, url_for
from flask import current_app as app
from flask_login import login_user, current_user

from flaskr import db
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
        # check credentials
        row_proxy = db.session.execute(db.select(User)
                    	               .where(User.email==form.email.data)
                                      ).first()
        user = row_proxy[0]
        if user is None:
            flash('this email is not registered')
        elif user.password == form.password.data:
            login_user(user)
            flash("user.is_active={}".format(user.is_active))
            flash("user = {}, user.is_authenticated={}"
                  .format(user, user.is_authenticated))
            flash("user = {}, user.is_authenticated={}"
                  .format(current_user, current_user.is_authenticated))
            flash('now logged in', 'message')
            return redirect(url_for('home_bp.home'))
        else:
            flash('incorrect password')

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
