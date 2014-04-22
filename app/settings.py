# Standard libs
import os

class Config(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    APP_DIR = os.path.abspath(os.path.dirname(__file__)) # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    EVENTS_DB_HOST = os.environ['EVENTS_DB_HOST']
    EVENTS_DB_NAME = os.environ['EVENTS_DB_NAME']
    EVENTS_DB_USER = os.environ['EVENTS_DB_USER']
    EVENTS_DB_PASSWORD = os.environ['EVENTS_DB_PASSWORD']

class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False

    BASIC_AUTH_USERNAME = os.environ['BASIC_AUTH_USERNAME']
    BASIC_AUTH_PASSWORD = os.environ['BASIC_AUTH_PASSWORD']
    BASIC_AUTH_FORCE = True

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True

