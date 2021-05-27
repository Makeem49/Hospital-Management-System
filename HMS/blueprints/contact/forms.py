from flask_wtf import Form
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import InputRequired, Length, Optional
from wtforms_components import EmailField


class ContactForm(Form):
    message = TextAreaField("Message", validators=[InputRequired(), Length(min=10, max=2000) ])
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=2, max=64)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=64)])
    email = EmailField("Email", validators=[InputRequired()])
    subject = StringField("Subject", validators=[Optional()])
    submit = SubmitField("Submit")