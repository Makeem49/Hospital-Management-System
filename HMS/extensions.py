from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import CsrfProtect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import  CsrfProtect


mail = Mail()
debugger = DebugToolbarExtension()
csrf = CsrfProtect()
db = SQLAlchemy()
csrf = CsrfProtect()
