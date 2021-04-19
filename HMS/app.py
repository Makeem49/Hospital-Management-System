from flask import Flask
from hms.blueprints.page import page 


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')

    app.register_blueprint(page)

    return app
