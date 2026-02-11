import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY","9f3c6a9a1b7f1e4c3e8f2a9d7b6c5f8a9d0e3f4c5a6b7c8d9e0f1a2b3c4d5e6")
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
