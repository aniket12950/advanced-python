from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.auth.models import User
from app.schemas import UserSchema

users_bp = Blueprint("users", __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@users_bp.route("/", methods=["GET"])
@jwt_required()
def get_users():
    users = User.query.all()
    return users_schema.dump(users)

@users_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user_schema.dump(user)
