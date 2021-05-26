from hms.blueprints.contact import contact
from flask import render_template
from hms.blueprints.contact.forms import ContactForm

@contact.route('/visitor')
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        email = form.email.data
        message = form.message.data
        name= form.name.data
        subject = form.subject.data
    return render_template('contact/contact.html', form=form)
