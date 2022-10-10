from flask import current_app as app
from flask import render_template

@app.route('/')
def index():
    # the landing page allowing login and registering users
    return render_template('index.html', title='Note App')

@app.route('/home')
def home():
    # the homepage of a user displaying his notes
    return render_template('home.html', title='Home')
    
@app.route('/login')
def login():
    # the login page
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    # the register page
    return render_template('register.html', title='Register')
    