from flask import Flask
from .extensions import db, login_manager, bcrypt
from .routes import main
from .auth import auth
from config import Config
from flask_login import LoginManager
from .models import User
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
def create_app():
    app = Flask(__name__,
                template_folder="templates",
                static_folder="static")
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
