# coding: utf-8
import json
from flask import jsonify, request
from flask.views import MethodView
from . import api
from .. import ma, oauth
from ..models import db, Todo


class TodoSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'title', 'priority', 'is_completed', '_links')

    # Smart hyperlinking
    _links = ma.Hyperlinks({
        'self': ma.URLFor('api.todo', id='<id>'),
        'collection': ma.URLFor('api.todos')
    })


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


class TodoApi(MethodView):
    def get(self, id):
        post = Todo.query.get_or_404(id)

        return todo_schema.jsonify(post)

    @oauth.require_oauth('email')
    def put(self, id):
        """
        update post with given id
        :param id:
        """
        current_user = request.oauth.user
        todo = Todo.query.get_or_404(id)

        if todo.user_id != current_user.id:
            return jsonify(error=True, message='Invalid access'), 401

        payload = json.loads(request.data)

        if 'title' in payload:
            todo.title = payload.get('title')

        if 'priority' in payload:
            todo.priority = payload.get('priority')

        if 'is_completed' in payload:
            todo.is_completed = payload.get('is_completed')

        db.session.commit()

        return jsonify(result='Operate successfully', todo=todo_schema.dump(todo).data)

    @oauth.require_oauth('email')
    def delete(self, id):
        current_user = request.oauth.user
        todo = Todo.query.get_or_404(id)

        if todo.user_id != current_user.id:
            return jsonify(error=True, message='Invalid access'), 401

        db.session.delete(todo)
        db.session.commit()

        return jsonify(result='Operate successfully')


class TodoListApi(MethodView):
    @oauth.require_oauth('email')
    def get(self):
        todos = Todo.query.all()
        result = todos_schema.dump(todos)

        return jsonify(todos=result.data)

    @oauth.require_oauth('email')
    def post(self):
        """
        create new post
        """
        current_user = request.oauth.user

        payload = json.loads(request.data)
        todo = Todo(title=payload.get('title'),
                    priority=payload.get('priority'),
                    is_completed=payload.get('is_completed'),
                    user_id=current_user.id)
        db.session.add(todo)
        db.session.commit()

        return jsonify(result='Operate successfully',
                       todo=todo_schema.dump(todo).data,
                       )


api.add_url_rule('/todo/<int:id>', view_func=TodoApi.as_view('todo'))
api.add_url_rule('/todos', view_func=TodoListApi.as_view('todos'))
