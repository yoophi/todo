# -*- coding: utf-8 -*-
from flask.ext.admin.contrib import sqla

from todo.database import db
from todo.extensions import admin
from .models import User, Role

admin.add_view(sqla.ModelView(User, session=db.session, name='User', category='User'))
admin.add_view(sqla.ModelView(Role, session=db.session, name='Role', category='User'))

