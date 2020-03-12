from flask import (
    Blueprint,
    jsonify
)
from flask_jwt_extended import jwt_required

""" API endpoints """
api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/get-full-address/<postal_code>', methods=['GET'])
@jwt_required
def get_full_address(postal_code):
    """Return a completete address for the give postal code"""
    from app.models.address import Address

    address = Address.find_one(postal_code)
    if address:
        return jsonify(address.to_dict())
    return jsonify(dict())
