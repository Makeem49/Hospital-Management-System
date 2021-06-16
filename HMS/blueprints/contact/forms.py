from flask_wtf import Form
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms_components import EmailField


class ContactForm(Form):
    message = TextAreaField('What\'s on your mind? ', validators=[DataRequired(), Length(min=10, max=2000)])
    name =  StringField('Name', validators=[DataRequired(), Length(2, 120)])
    email = EmailField("What's your email address?", validators=[DataRequired()])
    submit = SubmitField("Submit")

    
