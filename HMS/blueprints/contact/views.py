from hms.blueprints.contact import contact
from flask import render_template, redirect, url_for
from hms.blueprints.contact.forms import ContactForm


@contact.route('/contact', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        email = form.email.data
        message = form.message.data
        first_name= form.first_name.data
        last_name = form.last_name.data
        subject = form.subject.data
        data = {
            'message' : message,
            'first_name' : first_name,
            'last_name' : last_name,
            'email' : email
        }
        from hms.blueprints.contact.tasks import contact_task
        contact_task(email, subject, 'contact/email/index', data)
        return redirect(url_for('page.home'))
    return render_template('contact/contact.html', form=form)
