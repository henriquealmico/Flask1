from flask import Flask
from .extensions import db, migrate
from .config import Config

from app.Cao.model import cao_api
from app.cat.model import gato_api
from app.dono.model import dono_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(dono_api)
    app.register_blueprint(gato_api)
    app.register_blueprint(cao_api)

    return app