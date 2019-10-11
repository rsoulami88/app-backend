import os
from routes import *

flask_app.register_blueprint(items)
flask_app.register_blueprint(users)

if __name__ == '__main__':
    flask_app.run()
