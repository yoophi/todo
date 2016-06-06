from flask import Blueprint
from flask import render_template

core_bp = Blueprint('main', __name__)


@core_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@core_bp.route('/error')
def error():
    return 'ERROR_URI'
