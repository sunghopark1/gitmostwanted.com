from gitmostwanted.services import celery as service_celery, db as service_db, log as service_log
from flask import Flask
from os import environ

env = environ.get('GMW_APP_ENV', 'development').capitalize()

app = Flask(__name__)
app.config.from_object('gitmostwanted.config.Config' + env)
app.config.from_envvar('GMW_APP_SETTINGS', silent=True)

celery = service_celery.instance(app)
log = service_log.instance(app)
db = service_db.instance(app)

del Flask, service_celery, service_db, service_log, environ
