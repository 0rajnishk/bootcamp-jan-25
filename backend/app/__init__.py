# app/__init__.py
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# Initialize the database object
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    # Initialize JWT Manager
    jwt = JWTManager(app)


        # Enable CORS for the entire app
    CORS(app)  # This allows CORS for all routes by default


    # Enable CORS for specific routes
    # CORS(app, resources={r"/login": {"origins": "*"}, r"/signup": {"origins": "*"}})



    # Initialize the database (SQLAlchemy)
    db.init_app(app)

    # Import resources after app and db initialization to avoid circular imports
    from app.auth import signup_resource, login_resource
    from app.resources import TodoResource, HelloWorldResource

    # Register the routes
    app.add_url_rule('/signup', view_func=signup_resource, methods=['POST'])
    app.add_url_rule('/login', view_func=login_resource, methods=['POST'])
    app.add_url_rule('/todos', view_func=TodoResource.as_view('todos'))
    app.add_url_rule('/hello', view_func=HelloWorldResource.as_view('hello_world'))

    return app
