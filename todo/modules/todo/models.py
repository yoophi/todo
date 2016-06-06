from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from todo import db


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    priority = db.Column(db.Integer, default=3)
    is_completed = db.Column(db.Boolean(), default=False)

    user_id = db.Column(
        db.Integer,
        ForeignKey('users.id'),
        nullable=False,
    )
    user = relationship('User', backref='todos')

    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.title}>'.format(self=self)