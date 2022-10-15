"""The Application Factory"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import os

# global libraries
db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the flask app
    app = Flask(__name__, instance_relative_config=True,
             template_folder='templates')
    app.config.from_object('config.Config')
    app.config.from_object('config.Development')
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    
    with app.app_context():
        # import database models and create tables
        from .models import User, Note
        db.create_all()

        # import and register blueprints
        from .index import index
        from .auth import auth
        from .home import home
        app.register_blueprint(index.index_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(home.home_bp)

    return app
    