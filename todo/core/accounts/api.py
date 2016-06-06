# coding: utf-8
from flask import request, jsonify

from todo.core.api_1_0 import api
from todo.extensions import ma, oauth


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email')


user_schema = UserSchema()


@api.route('/users/self')
@oauth.require_oauth('email')
def users_self():
    """
    현재 사용자의 정보 가져오기
    ---
    tags:
      - Users
    parameters: []
    responses:
      '200':
        description: successful operation
        schema:
          $ref: '#/definitions/User'
    security:
      - oauth:
          - email
    """

    user = request.oauth.user

    return jsonify(user_schema.dump(user).data)
