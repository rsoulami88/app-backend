from routes.items import *
from routes.users import *
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
import os
import datetime

flask_app = Flask(__name__)  # Provide the app and the directory of the docs
CORS(flask_app)
flask_bcrypt = Bcrypt(flask_app)
jwt = JWTManager(flask_app)
flask_app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
flask_app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
flask_app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)