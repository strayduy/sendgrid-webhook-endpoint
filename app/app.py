# Third party libs
from flask import Flask
from flask.ext.basicauth import BasicAuth
from flask_sslify import SSLify

# Our libs
from .blueprints import webhook
from .database import EventsDB

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app):
    basic_auth = BasicAuth(app)
    sslify = SSLify(app)

    EventsDB.init(app.config)

def register_blueprints(app):
    app.register_blueprint(webhook.blueprint)

