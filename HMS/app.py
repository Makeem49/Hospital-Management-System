from flask import Flask
from hms.blueprints.page import page 
from hms.blueprints.contact import contact

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')

    app.register_blueprint(page)
    app.register_blueprint(contact)

    return app
