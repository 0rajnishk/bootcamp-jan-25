# app/__init__.py

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api

# Initialize the database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    # Initialize JWT Manager
    jwt = JWTManager(app)

    # Enable CORS for the entire app
    CORS(app)

    # Initialize the database (SQLAlchemy)
    db.init_app(app)

    # Import models here to make sure tables are created
    from app.models import User  # Import models to ensure tables are registered
    
    # Create the tables if they don't exist
    with app.app_context():
        db.create_all()  # This will create all the tables defined in the models if they don't exist

    # Initialize Flask-RESTful API
    api = Api(app)

    # Import resources after app and db initialization to avoid circular imports
    from app.auth import signup_resource, login_resource
    from app.resources import TodoResource, HelloWorldResource

    # Register the routes 
    app.add_url_rule('/signup', view_func=signup_resource, methods=['POST'])
    app.add_url_rule('/login', view_func=login_resource, methods=['POST'])

    
    api.add_resource(HelloWorldResource, '/hello')
    api.add_resource(TodoResource, '/todo', '/todo_id/<int:todo_id>')


    return app