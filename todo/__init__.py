#!/usr/bin/env python
# coding: utf-8
import os

from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore, Security

from todo.core.accounts.models import Role, User
from todo.database import db
from todo.extensions import oauth, cors, debug_toolbar, mail, swagger_ui, ma, config, admin
from todo.swagger import get_swagger_spec

__version__ = '0.1'

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=user_datastore)


def create_app_min(config_name='default'):
    template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    app = Flask(__name__, template_folder=template_folder)

    config.init_app(app)
    app.config.from_yaml(config_name=config_name,
                         file_name='app.yml',
                         search_paths=[os.path.dirname(app.root_path)])

    return app


def create_app(config_name='default'):
    """
    :param config_name: developtment, production or testing
    :return: flask application

    flask application generator
    """
    app = create_app_min(config_name)

    cors.init_app(app, resources={r"/api/v1.0/*": {"origins": "*"}})
    db.init_app(app)
    oauth.init_app(app)
    security.init_app(app)
    debug_toolbar.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    admin.init_app(app)
    swagger_ui.init_app(app, info={'title': 'Todo API'},
                        spec=get_swagger_spec(),
                        params={
                            'OAUTH_CLIENT_ID': 'swagger',
                            'OAUTH_CLIENT_SECRET': 'secret'
                        }, url_prefix='/swagger')

    from todo.core.views import core_bp as main_blueprint

    app.register_blueprint(main_blueprint)

    from core.api_1_0 import api as api_1_0_blueprint
    import todo.core.accounts.api
    import todo.modules.todo.api

    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    import todo.core.accounts.admin
    import todo.core.api_1_0.admin

    return app
