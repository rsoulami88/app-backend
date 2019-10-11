from flask import request
from controllers.listings import Items
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

items = Blueprint('items', __name__)


@items.route('/items/get_all', methods=['GET'])
@jwt_required
def get_items():
    return Items().get_all_item()


@items.route('/items/get_one', methods=['GET'])
@jwt_required
def get_one_item():
    _id = request.get_json()['_id']
    return Items().get_item(_id)


@items.route('/items/update_one', methods=['PUT'])
@jwt_required
def update_one_item():
    obj = request.get_json()
    return Items().update_item(obj)


@items.route('/items/delete_one', methods=['DELETE'])
@jwt_required
def delete_one_item():
    _id = request.get_json()['_id']
    return Items().delete_item(_id)
