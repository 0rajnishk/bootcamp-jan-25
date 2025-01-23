from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required

todos = []

class TodoResource(MethodView):

    @jwt_required()
    def get(self):
        return jsonify(todos)

    @jwt_required()
    def post(self):
        data = request.get_json()
        todos.append(data)
        return jsonify(data), 201



class HelloWorldResource(MethodView):
    def get(self):
        return jsonify({"message": "Hello, World!"})

    def post(self):
        return jsonify({"message": "post"})
