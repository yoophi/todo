#!/usr/bin/env python
# coding: utf-8
import logging
import os.path as op

from flask.ext.cors import CORS
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.mail import Mail
from flask.ext.oauthlib.provider import OAuth2Provider
from flask.ext.security import SQLAlchemyUserDatastore, Security

from .helpers import Flask
from .models import db, User, Role

__version__ = '0.1'

oauth = OAuth2Provider()
cors = CORS()

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=user_datastore)
debug_toolbar = DebugToolbarExtension()
mail = Mail()


logger1 = logging.getLogger('flask_oauthlib')
logger2 = logging.getLogger('oauthlib')
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.DEBUG)
file_handler1 = logging.FileHandler('flask_oauthlib.log')
file_handler2 = logging.FileHandler('oauthlib.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s = %(message)s')
file_handler1.setFormatter(formatter)
file_handler2.setFormatter(formatter)

logger1.addHandler(file_handler1)
logger2.addHandler(file_handler2)


def create_app(config_name):
    """
    :param config_name: developtment, production or testing
    :return: flask application

    flask application generator
    """
    template_folder = op.join(op.dirname(op.abspath(__file__)), 'templates')
    app = Flask(__name__, template_folder=template_folder)
    app.config.from_yaml(app.root_path)
    app.config.from_heroku()

    cors.init_app(app)
    db.init_app(app)
    # login_manager.init_app(app)
    oauth.init_app(app)
    security.init_app(app)
    debug_toolbar.init_app(app)
    mail.init_app(app)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    # from .auth import auth as auth_blueprint
    #
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api_1_0 import api as api_1_0_blueprint

    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app


# @login_manager.user_loader
# def load_user(user_id):
#     """Hook for Flask-Login to load a User instance from a user ID."""
#     return User.query.get(user_id)
