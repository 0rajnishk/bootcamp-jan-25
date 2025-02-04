# app/auth.py
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

# Import db and User model after app is initialized
from app import db
from app.models import User

# Signup route
def signup_resource():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if user already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'message': 'Username or Email already exists'}), 400
    role = 'manager'
    # Hash password and store in database
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password, role = role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# Login route
def login_resource():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Fetch user by email
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        # The JWT spec allows the sub claim (identity) to be a string
        user_id = str(user.id)
        access_token = create_access_token(identity=user_id)
        return jsonify({'message': 'Login successful', 'access_token': access_token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401
