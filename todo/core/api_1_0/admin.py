# -*- coding: utf8 -*-

from flask.ext.admin.contrib import sqla

from todo.database import db
from todo.extensions import admin
from .models import Client, Token

admin.add_view(sqla.ModelView(Client, session=db.session, name='Client', category='System'))
admin.add_view(sqla.ModelView(Token, session=db.session, name='Token', category='System'))
