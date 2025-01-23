from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask import current_app

def login_resource():
    username = request.json.get('username')
    password = request.json.get('password')

    # Verify credentials (this is a simple example, implement proper validation)
    if username == 'user' and password == 'password':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Invalid credentials"}), 401