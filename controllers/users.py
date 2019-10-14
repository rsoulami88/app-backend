from config.db import collection
from bson.json_util import dumps
from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from routes import *
from utils.register_controls import *
from utils.controls import *

flask_app = Flask(__name__)  # Provide the app and the directory of the docs
CORS(flask_app)
flask_bcrypt = Bcrypt(flask_app)
jwt = JWTManager(flask_app)


class Users(object):
    def __init__(self):
        self.collection = collection

    def login(self, obj):
        if find_in_request(obj, ["username", "password"]):
            username = obj['username']
            password = obj['password']
            user = list(self.collection.find({"username": username}))
            if len(user) > 0:
                pswd = user[0]['password']
                pw_hash = flask_bcrypt.check_password_hash(pswd, password)
                if pw_hash:
                    access_token = create_access_token(identity=username)
                    return dumps({'success': True, 'data': {'username': username, 'token': access_token}})
                else:
                    return dumps({'success': False, 'error': 401})
            else:
                return dumps({'success': False, 'error': 409})
        else:
            return dumps({'success': False, 'error': 400})

    def register(self, obj):
        if not find_in_request(obj, ["username", "password", "conf_password", "name"]):
            return dumps({'success': False, 'error': 400})
        else:
            if obj["password"] != obj["conf_password"]:
                return dumps({'success': False, 'error': 400})
            else:
                if 6 < len(obj["password"]) < 20 and num_there(obj["password"]) and special_there(obj["password"]):
                    user = list(self.collection.find({"username": obj["username"]}))
                    if len(user) > 0:
                        return dumps({'success': False, 'error': 404})
                    else:
                        dico = {"username": obj["username"],
                                "name": obj["name"],
                                "password": flask_bcrypt.generate_password_hash(obj["password"]).decode('utf-8')}
                        self.collection.insert_one(dico)
                        return dumps({'success': True})
                else:
                    return dumps({'success': False, 'error': 400})
