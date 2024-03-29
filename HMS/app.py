from flask import Flask
# from celery import Celery 

from hms.blueprints.page import page 
from hms.blueprints.user import user
from hms.blueprints.contact import contact
from hms.extensions import mail, debugger, csrf, login_manager, db


login_manager.login_view = 'users.login'
login_manager.session_protection = 'strong'
login_manager.login_message = 'You need to login to access the page'
login_manager.login_message_category = 'info'
login_manager.refresh_view = 'user.login'
login_manager.needs_refresh_message = "To protect your account, please re-authenticate to view this page"
login_manager.needs_refresh_message_category = 'info'





# CELERY_TASK_LIST = []

# def create_celery_app(app=None):
#     """
#     Create a new Celery object and tie together the Celery config to the app's
#     config. Wrap all tasks in the context of the application.

#     :param app: Flask app
#     :return: Celery app
#     """
#     app = app or create_app()

#     celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'],
#                     include=CELERY_TASK_LIST)
#     celery.conf.update(app.config)
#     TaskBase = celery.Task

#     class ContextTask(TaskBase):
#         abstract = True

#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return TaskBase.__call__(self, *args, **kwargs)

#     celery.Task = ContextTask
#     return celery



def create_app(settings_override = None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')

    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)
    app.register_blueprint(user)
    app.register_blueprint(contact)
    extensions(app)

    return app


def extensions(app):
    mail.init_app(app)
    debugger.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)