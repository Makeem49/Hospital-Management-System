from hms.blueprints.contact import contact
from flask import render_template
from hms.blueprints.contact.forms import ContactForm


@contact.route('/contact', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        email = form.email.data
        message = form.message.data
        name= form.name.data
        subject = form.subject.data
        data = {
            'message' : message,
            'name' : name,
            'email' : email
        }
        from hms.blueprints.contact.tasks import contact_task
        contact_task(email, subject, 'contact/email/index', data)
    return render_template('contact/contact.html', form=form)
