import os

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_graphql import GraphQLView

from app.models.address import db
from app.views.api import api
from app.schema import schema


def create_app():
    """Start a new flask app instance"""

    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Init DB
    db.init_app(app)

    # Init JWT
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(api)

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True # for having the GraphiQL interface
        )
    )

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '5000'), debug=True)

