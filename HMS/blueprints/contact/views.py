from hms.blueprints.contact import contact
from flask import render_template

@contact.route('/visitor')
def contact():
    return render_template('contact/contact.html')
