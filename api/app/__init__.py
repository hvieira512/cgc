from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .routes import api_bp

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    db.init_app(app)

    app.register_blueprint(api_bp, url_prefix="/api")
    return app
