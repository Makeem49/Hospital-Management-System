from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import CsrfProtect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy




mail = Mail()
debugger = DebugToolbarExtension()
csrf = CsrfProtect()
login_manager = LoginManager()
db = SQLAlchemy()