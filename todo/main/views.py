# -*- coding: utf8 -*-
import inspect
import os
import json
from urlparse import urlparse

import yaml
from flask import render_template, jsonify, current_app, url_for
from flask.ext.cors import cross_origin
from flask.ext.swagger import swagger

from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/swagger.json', methods=['GET'])
@cross_origin()
def swagger_json():
    swagger_file = os.path.join(current_app.root_path, 'swagger.json')
    with open(swagger_file) as data_file:
        data = json.load(data_file)

    return jsonify(data)


@main.route('/spec')
@cross_origin()
def spec():
    """
    info:
      title: Todo API
      description: Todo API 서버입니다
      termsOfService: http://swagger.io/terms
      contact:
        email: yoophi@gmail.com
    host: {host}
    basepath: /api/v1.0
    schemes:
      - http
    produces:
      - application/json
    tags:
      - name: todo
        description: Everything about your Todos
        externalDocs:
          description: Find out more
          url: 'http://swagger.io'
      - name: user
        description: Operations about user
        externalDocs:
          description: Find out more
          url: 'http://swagger.io'
    definitions:
      Todo:
        type: object
        required:
          - title
          - is_completed
        properties:
          id:
            type: integer
          title:
            type: string
          is_completed:
            type: boolean
            default: false
          _links:
            type: object
            properties:
              collection:
                type: string
              self:
                type: string
      User:
        type: object
        properties:
          id:
            type: integer
            format: int64
          email:
            type: string
    securityDefinitions:
      petstore_auth:
        type: oauth2
        authorizationUrl: {auth_url}
        flow: implicit
        scopes:
          email: User 및 Todo 에 대한 기본 작업에 대한 권한
    externalDocs:
      description: Find out more about Swagger
      url: 'http://swagger.io'
    """
    swag = swagger(current_app)
    swag.update(yaml.load(inspect.getdoc(spec).format(
        auth_url=url_for('api.user_authorize', _external=True),
        host=(get_netloc()),
    )))
    return jsonify(swag)


def get_netloc():
    parsed_url = urlparse(url_for('main.spec', _external=True))
    return parsed_url.netloc
