from ast import Pass
from flask_wtf import FlaskForm, Recaptcha
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('e-mail', validators=[DataRequired(), Email('invalid email address')])
    password = PasswordField('password', validators=[DataRequired()])
    recaptcha = Recaptcha()
    submit = SubmitField('Submit')
