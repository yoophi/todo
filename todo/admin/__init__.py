import os

from flask.ext.admin import Admin

from ..helpers import Flask
from ..models import db

admin = Admin()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_yaml(os.path.dirname(app.root_path))
    app.config.from_heroku()

    db.init_app(app)
    admin.init_app(app)

    from . import views

    return app
