from flask import request
from controllers.users import Users
from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/users/login', methods=['POST'])
def login():
    obj = request.get_json()
    return Users().login(obj)


@users.route('/users/register', methods=['POST'])
def register():
    obj = request.get_json()
    return Users().register(obj)

