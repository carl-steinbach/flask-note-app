"""The Application Factory"""

from flask import Flask
import os 

# global libraries

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
    
    with app.app_context():
        # import and register blueprints
        from .index import index
        from .auth import auth
        from .home import home
        app.register_blueprint(index.index_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(home.home_bp)

    return app
    