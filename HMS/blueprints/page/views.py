from flask import render_template
from hms.blueprints.page import page


@page.route('/')
def home():
    return render_template('page/home.html')


@page.route('/contact')
def contact():
    return render_template('page/contact.html')

@page.route('/blog')
def blog():
    return render_template('page/blog.html')