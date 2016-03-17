import os
from flask import Flask
from flask.ext.admin import Admin
from app.database import db
from flask.ext.admin.contrib import sqla
from app.main.models import User


def create_app(conf=None):
    app = Flask(__name__)
   
    # Init DB
    db.init_app(app)

    # Register blueprints
    from app.main.views import main
    app.register_blueprint(main)

    from app.admin import create_admin
    admin=create_admin(app)

    return app
