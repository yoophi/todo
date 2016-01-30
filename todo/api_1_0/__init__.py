from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

from . import authentication, users, todos


@api.route('/sample')
def do_sample():
    return jsonify({'result': 'sample'})
