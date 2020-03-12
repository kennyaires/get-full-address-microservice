from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from app.views.api import api


def create_app():
    """Start a new flask app instance"""

    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Init DB
    db = SQLAlchemy(app)

    # Init JWT
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(api)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=False)

