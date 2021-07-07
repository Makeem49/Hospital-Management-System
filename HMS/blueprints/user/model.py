from enum import unique
from hms.extensions import db 
from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hms.extensions import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

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
    date_or_birth = db.Column(db.DateTime(), nullable = True)
    state_of_origin = db.Column(db.String(64), nullable=True)
    place_of_birth = db.Column(db.String(64), nullable=True)
    address = db.Column(db.String(120), nullable = True)
    gender = db.Column(db.String(10), nullable = True)

    # Patient login credentials 
    username = db.Column(db.String(64), nullable = True, unique = True)
    email = db.Column(db.String(120), nullable=False, unique = True)
    password_hash = db.Column(db.String(128))

    # Account status
    active = db.Column(db.Integer, server_default = '1', nullable = False)
    confirmed = db.Column(db.Bolean, default = False)


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

    def serialize_confirmation_token(self, expiration=500):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'confirm' : self.id}).decode('utf-8')

    def disserialize_confirmation_token(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.commit()

        return User.query.get(data.get('confirm'))

    def generate_reset_password(self, expiration=500):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'confirm' : self.id}).decode('utf-8')

    @staticmethod
    def reset_pasword(token):
        s = Serializer(current_app.config['SECRET_KEY'])

        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        return User.query.get(data.get('confirm'))

    def generate_email_token(self, email, expiration=500):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'confirm' : self.id, 'new_email' : email})

    def confirm_email_token(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])

        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        
        user = User.query.get(data.get('confirm'))
        new_email = User.query.get(data.get('new_email'))

        if data.get('confirm') != self.id:
            return False

        if User.query.filter_by(email = new_email ).first():
            return False

        if user is None:
            return False

        user.email = new_email
        db.session.add(self)

        return True
        


    


        

        