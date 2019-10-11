from config.db import collection
from bson.json_util import dumps
from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from routes import *
from utils.register_controls import *

flask_app = Flask(__name__)  # Provide the app and the directory of the docs
CORS(flask_app)
flask_bcrypt = Bcrypt(flask_app)
jwt = JWTManager(flask_app)


class Users(object):
    def __init__(self):
        self.collection = collection

    def login(self, obj):
        username = obj['username']
        password = obj['password']
        keys = list(obj.keys())
        if 'username' not in keys:
            return dumps({'success': False, 'error': 400})
        elif 'password' not in keys:
            return dumps({'success': False, 'error': 400})
        else:
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
                return dumps({'success': False, 'error': 404})

    def register(self, obj):
        keys = list(obj.keys())
        if 'username' not in keys:
            return dumps({'success': False, 'error': 400})
        #elif 'email' not in keys:
            #return dumps({'success': False, 'error': 400})
        #elif 'phone' not in keys:
            #return dumps({'success': False, 'error': 400})
        elif 'name' not in keys:
            return dumps({'success': False, 'error': 400})
        elif 'password' not in keys:
            return dumps({'success': False, 'error': 400})
        elif 'conf_password' not in keys:
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
                                #"phone": obj["phone"],
                                #"email": obj["email"],
                                "password": flask_bcrypt.generate_password_hash(obj["password"]).decode('utf-8')}
                        self.collection.insert_one(dico)
                        return dumps({'success': True})
                else:
                    return dumps({'success': False, 'error': 400})
