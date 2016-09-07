# pylint: disable=C1001
class Config:
    # Custom
    DEBUG_FILE = '/tmp/gmw.log'

    # Flask
    PERMANENT_SESSION_LIFETIME = 1209600  # 14 days
    SECRET_KEY = ''
    TESTING = False
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_RECYCLE = 3600
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery
    CELERY_TIMEZONE = 'Europe/Berlin'
    CELERY_BROKER_URL = ''
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']

    # Oauth
    GITHUB_AUTH = (None, None)


class ConfigDevelopment(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


class ConfigTesting(Config):
    SECRET_KEY = 'testing'  # noqa
    TESTING = True


class ConfigProduction(Config):
    DEBUG = False
