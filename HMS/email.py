from hms.extensions import mail 
from flask import current_app, render_template
from flask_mail import Message
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def contact_me(email, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(sender=email, recipients=[app.config['MAIL_USERNAME']], reply_to=email, subject=subject)
    msg.body = render_template(template + '.txt' , **kwargs)
    mail.send(msg)
    # thr = Thread(target=send_async_email, args=[app, msg])
    # thr.start()
    # return thr


