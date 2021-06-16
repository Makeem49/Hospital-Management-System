from flask import Blueprint

contact = Blueprint("contact", __name__, template_folder="templates")

from hms.blueprints.contact import views
