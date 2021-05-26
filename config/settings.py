DEBUG = True

SECRET_KEY = "kjhskihfoinehrc"

SQLALCHEMY_DATABASE_URI = ''
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False


# Celery.
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5


# SQLAlchemy 
# db_uri = 'postgresql://makeem49:Olayinka1?@localhost:7000/hms'

# db_uri = 'postgresql://postgres:Olayinka1?@localhost:5432/snakeeyes'