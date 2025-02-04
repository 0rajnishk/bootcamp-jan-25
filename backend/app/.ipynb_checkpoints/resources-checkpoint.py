from flask import jsonify, request
# from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager
from flask_restful import Resource
from app.models import User, Tasks
todos = []


class HelloWorldResource(Resource):
    @jwt_required()
    def get(self):
        email = get_jwt_identity()
        print(email)
        return jsonify({"message": "Hello, World!", "email":email})

    def post(self):
        return jsonify({"message": "post"})


class TodoResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        print("user_id", user_id)
        try:
            user = User.query.filter(User.id == user_id).first()  
            print(user)
            print(user.serialize())
            
        except Exception as e:
            print(e)
        
        return jsonify({"message": "Hello, World!", "data":[1, 2, 3, 4, 5] })

    def post(self):
        return jsonify({"message": "post"})


class TaskResource(Resource):
    @jwt_required()
    def get(self):
        """Get all tasks (for managers or team leads)"""
        
        user_id = get_jwt_identity()
        current_user = User.query.filter_by(id=user_id).first()
        role = current_user['role']

        if role not in ['manager', 'teamlead']:
            return {"message": "You are not authorized to view tasks"}, 403

        tasks = Task.query.all()
        tasks_list = [{"id": task.id, "title": task.title, "description": task.description, "status": task.status} for task in tasks]
        
        return {"tasks": tasks_list}

    @jwt_required()
    def post(self):
        """Create a new task (for managers or team leads)"""
        data = request.get_json()
        user_id = get_jwt_identity()
        current_user = User.query.filter_by(id=user_id).first()
        role = current_user['role']

        if role not in ['manager', 'teamlead']:
            return {"message": "You are not authorized to create tasks"}, 403

        # Create the new task
        new_task = Task(
            title=data['title'],
            description=data['description'],
            status=data.get('status', 'assigned'),
            assigned_to=data['assigned_to'],
            created_by=current_user['id'],
            due_date=data.get('due_date', None)
        )
        db.session.add(new_task)
        db.session.commit()

        return {"message": "Task created successfully", "task_id": new_task.id}, 201

    @jwt_required()
    def put(self, task_id):
        """Update task status (for assigned users or team leads)"""
        data = request.get_json()
        user_id = get_jwt_identity()
        current_user = User.query.filter_by(id=user_id).first()
        role = current_user['role']

        # Fetch the task
        task = Task.query.get(task_id)
        if not task:
            return {"message": "Task not found"}, 404
        
        if role == 'manager' or (role == 'teamlead' and task.assigned_to == current_user['id']):
            # Update task status
            task.status = data.get('status', task.status)
            db.session.commit()
            return {"message": "Task status updated successfully"}, 200
        else:
            return {"message": "You are not authorized to update this task"}, 403

    @jwt_required()
    def get_task_by_user(self):
        """Get tasks assigned to the current user"""
        user_id = get_jwt_identity()
        current_user = User.query.filter_by(id=user_id).first()
        tasks = Task.query.filter_by(assigned_to=current_user['id']).all()

        tasks_list = [{"id": task.id, "title": task.title, "description": task.description, "status": task.status} for task in tasks]
        
        return {"tasks": tasks_list}


# Task Resource with the specific task ID for updating and getting details of a single task
class TaskDetailResource(Resource):
    @jwt_required()
    def get(self, task_id):
        """Get details of a specific task (for authorized users)"""
        task = Task.query.get(task_id)
        if not task:
            return {"message": "Task not found"}, 404
        
        user_id = get_jwt_identity()
        current_user = User.query.filter_by(id=user_id).first()
        role = current_user['role']

        # Check if the current user is authorized to view the task
        if task.assigned_to == current_user['id'] or role in ['manager', 'teamlead']:
            task_data = {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "status": task.status,
                "assigned_to": task.assigned_user.username,
                "created_by": task.creator_user.username,
                "due_date": task.due_date
            }
            return {"task": task_data}
        
        return {"message": "You are not authorized to view this task"}, 403


# Update task status (for authorized users only)
class TaskStatusResource(Resource):
    @jwt_required()
    def put(self, task_id):
        """Update status of a task (for assigned user/team lead/manager)"""
        task = Task.query.get(task_id)
        if not task:
            return {"message": "Task not found"}, 404
        
        user_id = get_jwt_identity()
        current_user = User.query.filter_by(id=user_id).first()
        role = current_user['role']

        # Check if the user is authorized to update the task status
        if task.assigned_to == current_user['id'] or role in ['manager', 'teamlead']:
            task.status = request.json.get('status', task.status)
            db.session.commit()
            return {"message": "Task status updated successfully"}, 200
        
        return {"message": "You are not authorized to update this task"}, 403


# Resource for changing user roles (manager/teamlead)
class UserRoleResource(Resource):
    @jwt_required()
    def put(self, user_id):
        """Update a user's role (Only manager can change roles)"""
        user_id = get_jwt_identity()
        current_user = User.query.filter_by(id=user_id).first()

        if current_user['role'] != 'manager':
            return {"message": "You are not authorized to change roles"}, 403

        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        
        new_role = request.json.get('role', user.role)
        user.role = new_role
        db.session.commit()

        return {"message": f"User role updated to {new_role}"}, 200



