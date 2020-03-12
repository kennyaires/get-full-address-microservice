from flask_sqlalchemy import SQLAlchemy
from main import create_app

db = SQLAlchemy(create_app())


class Address(db.Model):
    """Address model"""
    __tablename__ = 'Address'
    postal_code = db.Column('postal_code', db.Unicode, primary_key=True)
    address = db.Column('address', db.Unicode)
    neighborhood = db.Column('neighborhood', db.Unicode)
    city = db.Column('city', db.Unicode)
    state = db.Column('state', db.Unicode)

    def __init__(self, postal_code, address=None, neighborhood=None, city=None, state=None):
        self.postal_code = postal_code
        self.address = address
        self.neighborhood = neighborhood
        self.city = city
        self.state = state

    def __str__(self):
        return f'{self.address}, {self.neighborhood}, {self.city} - {self.state}'

    def to_dict(self):
        _dict = {
            'postal_code': self.postal_code,
            'address': self.address,
            'neighborhood': self.neighborhood,
            'city': self.city,
            'state': self.state,
        }
        return _dict

    @classmethod
    def find_one(cls, postal_code):
        """Find one address object from postal code"""
        return cls.query.filter_by(postal_code=postal_code).first()
