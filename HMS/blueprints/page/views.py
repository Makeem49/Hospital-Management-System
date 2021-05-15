from flask import render_template
from hms.blueprints.page import page


@page.route('/')
def home():
    return render_template('page/home.html')


@page.route('/doctor')
def doctor():
    return render_template('page/doctors.html')

@page.route('/department')
def department():
    return render_template('page/department.html')

@page.route('/blog')
def about():
    return render_template('page/about.html')


@page.route('/faq')
def questions():
    pass




