import os 
DEBUG = True

SECRET_KEY = 'fe84032a3161e31057e4d7630ce73f25'
SERVER_NAME = 'localhost:7000'

# db_uri = 'postgresql://makeem49:Olayinka1?@localhost:7000/hms'
# SQLALCHEMY_DATABASE_URI = db_uri
# SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False


# Celery.
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5


# flask-mail configuration 
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = '587'
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_USERNAME')
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_PASSWORD')
FLASKY_MAIL_SUBJECT_PREFIX = 'Dr. Poo clinic'
FLASKY_MAIL_SENDER = os.environ.get('MAIL_USERNAME')
