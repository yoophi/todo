import os
import json
from flask import render_template, jsonify, current_app
from flask.ext.cors import cross_origin

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