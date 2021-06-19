from enum import unique
from hms.extensions import db 
from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hms.extensions import login_manager

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin,db.Model): 
    __tablename__ = 'users'

    # Unique identifier
    id = db.Column(db.Integer, primary_key=True, unique=True)

    # Patient data
    firstName = db.Column(db.String(32), nullable = False)
    lastName = db.Column(db.String(32), nullable = False)
    otherName = db.Column(db.String(32), nullable = True, server_default='')
    date_or_birth = db.Column(db.DateTime(), nullable = False)
    state_of_origin = db.Column(db.String(64), nullable=False)
    place_of_birth = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(120), nullable = False)
    gender = db.Column(db.String(10), nullable = False)

    # Patient login credentials 
    username = db.Column(db.String(64), nullable = True, unique = True)
    email = db.Column(db.String(120), nullable=False, unique = True)
    password_hash = db.Column(db.String(128))

    # Account status
    active = db.Column(db.Integer, server_default = '1', nullable = False)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")


    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password): 
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """ Help to check whether the account is still active or not."""
        return self.active

    @classmethod
    def find_by_identity(cls, identity):
        return User.query.filter((User.email == identity ) | (User.username == identity)).first()
