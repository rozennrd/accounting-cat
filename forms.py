from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField



class SignUpForm(FlaskForm):
    username = StringField('UserName')
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('UserName')
    password = PasswordField('Password')
    submit = SubmitField('Log In')
