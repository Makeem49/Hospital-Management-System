from flask import render_template
from hms.blueprints.page import page


@page.route('/')
def home():
    return render_template('page/home.html')