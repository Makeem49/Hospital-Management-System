from flask import flash, redirect, render_template, url_for, request
from hms.blueprints.contact import contact
from hms.blueprints.contact.forms import ContactForm
from hms.email import contact_me


@contact.route('/contact', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        print(form.email.data)
        name = form.email.data
        email = form.email.data
        message = form.message.data

        data = {
            'name' : name,
            'email' : email,
            'message' : message
        }

        contact_me(email, "Contact message.", '/contact/mail/index', data=data)
        flash("Thank you for contacting us, your message has been delivered.", 'success')
        return redirect(url_for("page.home"))
    return render_template('contact/index.html', form = form )



