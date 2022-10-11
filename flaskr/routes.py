from flask import current_app as app, request, url_for, redirect, flash
from flask import render_template
from flaskr.forms import LoginForm

@app.route('/')
def index():
    # the landing page allowing login and registering users
    return render_template('index.html', title='Note App')

@app.route('/home')
def home():
    # the homepage of a user displaying his notes
    return render_template('home.html', title='Home')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    # the login page
    form = LoginForm()
    if form.validate_on_submit():
        flash('now logged in', 'message')
        return redirect(url_for(home))

    return render_template('login.html', title='Login', form=form)

@app.route('/register')
def register():
    # the register page
    return render_template('register.html', title='Register')
