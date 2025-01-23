from flask import Flask
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    # Initialize JWT Manager
    jwt = JWTManager(app)

    # Initialize resources
    from .auth import login_resource
    from .resources import TodoResource, HelloWorldResource

    # Register the routes
    app.add_url_rule('/login', view_func=login_resource)
    app.add_url_rule('/todos', view_func=TodoResource.as_view('todos'))
    app.add_url_rule('/hello', view_func=HelloWorldResource.as_view('hello_world'))
    return app
