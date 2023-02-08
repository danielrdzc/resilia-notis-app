from flask import Blueprint, jsonify, request

test_bp = Blueprint('test_bp', 'test_bp', url_prefix='/api')

@test_bp.route('/test', methods=['GET'])
def test():
    data = 'testing api'
    response = jsonify(data)
    return response