from flask import Flask, jsonify
from api.endpoints import API_BLUEPRINT
from flask_migrate import Migrate
from models import db

def create_app(app_settings):
    app = Flask(__name__)
    app.config.from_object(app_settings)

    @app.route("/")
    def index():
        return "Birthday API"

    app.register_blueprint(API_BLUEPRINT)
    db.init_app(app)

    return app
