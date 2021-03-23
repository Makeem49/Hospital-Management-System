from flask import Blueprint

page = Blueprint('page', __name__, template_folder='templates')

from hms.blueprints.page import views


