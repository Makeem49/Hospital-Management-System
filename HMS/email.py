from hms.extensions import mail 
from flask import app, current_app, render_template
from flask_mail import Message

def contact_me(email, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(sender=email, recipients=app.config['MAIL_USERNAME'], reply_to=email, subject=subject)
    msg.body = render_template(template + '.txt' , **kwargs)
    mail.send(msg)

