from flask import Blueprint, render_template, flash, redirect, url_for
from flask import current_app as app
from flaskr.forms import LoginForm, RegistrationForm
from flaskr import db
from flaskr.models import User

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
        # check credentials
        result = db.session.execute(db.select(User)
                    	            .where(User.email==form.email.data))
        user_data = result.first()[0]
        if user_data is None:
            flash('this email is not registered')
        elif user_data.password == form.password.data:
            flash('now logged in', 'message')
            return redirect(url_for('home_bp.home'))       
        else:
            flash('incorrect password')

    return render_template('login.html', title='Login', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # the register page
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
                            password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('account created', 'message')
            return redirect(url_for('auth_bp.login'))

    return render_template('register.html', title='Register', form=form)
