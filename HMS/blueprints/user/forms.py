from flask_wtf import Form
from flask_wtf.recaptcha import validators
from wtforms import (
    StringField, 
    PasswordField, 
    BooleanField, 
    SubmitField
)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, InputRequired
from wtforms_components import EmailField


class LoginForm(Form):
    email = EmailField("Email", validators=[DataRequired(), Length(min=4, max=120)])
    password = PasswordField("Password", validators=[DataRequired(), 
                                Length(min=8, max=24, message="Your password must be between 8-24 character long.")])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField('Login')


class RegisterForm(Form):
    first_name = StringField("First name", validators=[DataRequired(), 
                                Length(min=2, max=24, message="Name length must be between 2-24 character long")])
    last_name = StringField("First name", validators=[DataRequired(), 
                                Length(min=2, max=24, message="Name length must be between 2-24 character long")])
    other_name = StringField("First name", validators=[DataRequired(), 
                                Length(min=2, max=24, message="Name length must be between 2-24 character long")])
    date_of_birth = DateField("Date of Birth", validators=[InputRequired()], format='%Y-%m-%d')         
    