from flask import Flask
from flask_bcrypt import Bcrypt
from config import Config


bcrypt = Bcrypt() 


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    bcrypt.init_app(app)

    from .main.views import main
    app.register_blueprint(main)

    from .auth.views import auth
    app.register_blueprint(auth)

    return app
