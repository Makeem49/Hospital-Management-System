from flask import Blueprint

user = Blueprint("user", __name__, template_folder='templates')

from hms.blueprints.user import views
