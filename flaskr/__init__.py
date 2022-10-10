"""The Application Factory"""

import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True,
             template_folder='templates')
    app.config.from_object('config.Config')
    app.config.from_object('config.Development')
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    with app.app_context():
        from . import routes

    return app
    