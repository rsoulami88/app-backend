import os
from flask import Flask
from flask_cors import CORS
import datetime
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from routes.items import *
from routes.users import *
from routes import flask_app

#flask_app = Flask(__name__)  # Provide the app and the directory of the docs
#CORS(flask_app)
#flask_bcrypt = Bcrypt(flask_app)
#jwt = JWTManager(flask_app)
#flask_app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#flask_app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
#flask_app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
flask_app.register_blueprint(items)
flask_app.register_blueprint(users)

if __name__ == '__main__':
    flask_app.run(port=int(os.environ.get('PORT', 5000)))
