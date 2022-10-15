from os import environ, path
from dotenv import load_dotenv
import os

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    SECRET_KEY = environ.get('SECRET_KEY', 'default_key')
    RECAPTCHA_PUBLIC_KEY = environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_SECRET_KEY = environ.get('RECAPTCHA_SECRET_KEY')
    TEMPLATES_FOLDER = 'templates'
    STATIC_FOLDER = 'static'
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(basedir + 'note.db'))

class Development:
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

class Production:
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
