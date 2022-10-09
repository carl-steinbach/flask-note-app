class Config:
    SECRET_KEY = '92h23hf98haf8'

class Development:
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

class Production:
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
