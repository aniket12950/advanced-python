from flask import Flask
from config import Config
from .extensions import db, jwt
from .auth.routes import auth_bp
from .users.routes import users_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(users_bp, url_prefix="/api/users")

    @app.route("/")
    def home():
        return {"message": "Flask API Running Successfully "}

    with app.app_context():
        db.create_all()

    return app
