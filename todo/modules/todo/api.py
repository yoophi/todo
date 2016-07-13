# coding: utf-8
import json

from flask import jsonify, request
from flask.views import MethodView

from todo.core.api_1_0 import api
from todo.database import db
from todo.extensions import ma
from todo.extensions import oauth
from .models import Todo


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
        """
        해당 Todo 가져오기
        ---
        parameters:
          - name: id
            description: Todo ID
            in: path
            type: integer
            required: true
        tags:
          - todo
        responses:
          '200':
            description: OK
            schema:
              $ref: '#/definitions/Todo'
        """
        post = Todo.query.get_or_404(id)

        return todo_schema.jsonify(post)

    @oauth.require_oauth('email')
    def put(self, id):
        """
        해당 Todo 수정
        ---
        tags:
          - todo
        security:
          - oauth:
              - email
        parameters:
          - name: id
            description: Todo ID
            in: path
            type: integer
            required: true
          - name: body
            in: body
            description: 수정하고 싶은 Todo JSON
            schema:
              type: object
              properties:
                title:
                  type: string
                priority:
                  type: integer
                  default: 1
                is_completed:
                  type: boolean
                  default: true
            required: true
        responses:
          '200':
            description: OK
            schema:
              type: object
              properties:
                result:
                  type: string
                todo:
                  $ref: '#/definitions/Todo'
        """
        current_user = request.oauth.user
        todo = Todo.query.get_or_404(id)

        if todo.user_id != current_user.id:
            return jsonify(error=True, message='Invalid access'), 401

        payload = json.loads(request.data)

        for key in ('title', 'priority', 'is_completed', ):
            if key in payload:
                setattr(todo, key, payload.get(key))

        db.session.add(todo)
        db.session.commit()

        return jsonify(result='Operate successfully', todo=todo_schema.dump(todo).data)

    @oauth.require_oauth('email')
    def delete(self, id):
        """
        해당 Todo 삭제
        ---
        parameters:
          - name: id
            description: Todo ID
            in: path
            type: integer
            required: true
        tags:
          - todo
        security:
          - oauth:
              - email
        responses:
          '200':
            description: OK
            schema:
              type: object
              properties:
                result:
                  type: string
        """
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
        """
        Get Todo List
        사용자의 Todo 목록을 가져온다.
        ---
        tags:
          - todo
        responses:
          200:
            description: OK
            schema:
              type: object
              properties:
                todos:
                  type: array
                  items:
                    $ref: '#/definitions/Todo'
        security:
          - oauth:
              - email
        """
        todos = Todo.query.all()
        result = todos_schema.dump(todos)

        return jsonify(todos=result.data)

    @oauth.require_oauth('email')
    def post(self):
        """
        새로운 Todo 생성
        ---
        tags:
          - todo
        security:
          - oauth:
              - email
        parameters:
          - name: body
            in: body
            description: 새로 생성하고 싶은 Todo JSON
            schema:
              type: object
              properties:
                title:
                  type: string
                priority:
                  type: integer
                  default: 1
            required: true
        responses:
          '200':
            description: OK
            schema:
              type: object
              properties:
                result:
                  type: string
                todo:
                  $ref: '#/definitions/Todo'
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
