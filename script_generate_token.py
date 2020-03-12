from main import create_app
from flask_jwt_extended import JWTManager, create_access_token

import config


def generate_token_for_app(app_name):
    """Generate access token for API usage"""
    app = create_app()
    with app.app_context():
        if app_name in config.ALLOWED_APPS:
            jwt = JWTManager(create_app())
            return jwt._create_access_token(identity=app_name, expires_delta=False)

    return 'App entered is not allowed.'

if __name__ == "__main__":
    """Generate access token for API usage"""
    print(generate_token_for_app('employee_register'))
