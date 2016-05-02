# coding: utf-8

from flask import request, jsonify
from . import api
from .. import oauth


@api.route('/me')
@oauth.require_oauth('email')
def me():
    """
    현재 사용자의 정보 가져오기
    ---
    tags:
      - user
    parameters: []
    responses:
      '200':
        description: successful operation
        schema:
          $ref: '#/definitions/User'
    security:
      - petstore_auth:
          - email
    """
    user = request.oauth.user
    return jsonify(id=user.id, email=user.email)


