from os import path
import yaml


def get_swagger_spec():
    _current_dir = path.dirname(path.abspath(__file__))

    with open(path.join(_current_dir, 'swagger.yaml'), 'r') as spec_file:
        return yaml.load(spec_file.read())

