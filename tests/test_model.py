from unittest import TestCase

from todo import create_app
from todo.core.accounts.models import User
from todo.core.api_1_0.models import Token
from todo.database import db


class TestUserModel(TestCase):
    def setUp(self):
        super(TestUserModel, self).setUp()

        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

    def test_xxx(self):
        from sqlalchemy.dialects import postgresql
        # >>> print str(q.statement.compile(dialect=postgresql.dialect()))
        # SELECT DISTINCT ON (name.value) name.id, name.value
        # FROM name ORDER BY name.value

        q = db.session.query(User).join(Token)
        # db.session.query(User).all()
        print str(q.statement.compile(dialect=postgresql.dialect()))

        # print str(q)
