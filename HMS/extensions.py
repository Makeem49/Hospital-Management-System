from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import CsrfProtect



mail = Mail()
debugger = DebugToolbarExtension()
csrf = CsrfProtect()
