from flask_wtf import Form
from flask_wtf.recaptcha import validators
from wtforms import (
    StringField, 
    PasswordField, 
    BooleanField, 
    SubmitField
)
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, InputRequired, Regexp, EqualTo, ValidationError
from wtforms_components import EmailField
from hms.blueprints.user.model import User


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

    email = EmailField("Email", validators=[DataRequired(), Length(min=4, max=120)])
    username = StringField("username", validators=[DataRequired(), Length(min=8, max=24), 
                                Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, ''numbers, dots or underscores')]) 
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=24)])
    conform_password = PasswordField("Password", validators=[DataRequired(), EqualTo("password", message='Pasword must match not match') ])
    submit = SubmitField('Register')

    # Custom validator methods
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("This email has already bearing register with an account")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("There's a user with this username.")
            

class UpdatePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[DataRequired(), Length(min=8, max=24)])
    new_password = PasswordField('New password', validators=[DataRequired(), Length(8, 24)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), Length(8, 24)])
    submit = SubmitField('Change passsword')

class UpdateEmailForm(Form):
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 24)])
    email = EmailField("New email", validators=[DataRequired(), Length(min=4, max=120)])
    submit = SubmitField('Change email')


class PasswordResetForm(Form):
    email = EmailField('Email', validators=[DataRequired(), Length(8, 24)])
    submit = SubmitField('Request for password reset link')

class ChangePasswordForm(Form):
    new_password = PasswordField('New password', validators=[DataRequired(), Length(8, 24)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), Length(8, 24)])
    submit = SubmitField('Change passsword')

