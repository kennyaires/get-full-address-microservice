import os

SQLALCHEMY_DATABASE_URI = f'sqlite:////{os.path.abspath("ceps.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

ALLOWED_APPS = ['employee_register']
