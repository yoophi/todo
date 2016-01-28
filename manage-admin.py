#!/usr/bin/env python
# coding: utf-8

import os

from flask.ext.script import Manager

from todo.admin import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
