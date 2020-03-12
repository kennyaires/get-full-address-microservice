import os

SQLALCHEMY_DATABASE_URI = f'sqlite:////{os.path.abspath("ceps.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
JWT_SECRET_KEY = '#AHPDAS!NDsadasd9ASND98@SPNDNASD9ASDAsaDKdsD3SA2De2323e'

ALLOWED_APPS = ['employee_register']
