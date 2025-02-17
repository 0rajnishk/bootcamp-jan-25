# app/models.py
from app import db




# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  # Store hashed password
    role = db.Column(db.String(50), nullable=False)  # Role: manager, teamlead, or member

    def __repr__(self):
        return f'<User, {self.username}>'

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'role': self.role
        }
    

# Ensure this is the correct model definition.
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(120), nullable=False, default="assigned")
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Created by user
    due_date = db.Column(db.Date, nullable=True)  # Due date for the task

    # Optionally, you can define relationships (if needed)
    assigned_user = db.relationship('User', foreign_keys=[assigned_to])
    creator_user = db.relationship('User', foreign_keys=[created_by])

    def __repr__(self):
        return f'<Task {self.title}>'

    def serialize(self):
        return {
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'assigned_to': self.assigned_to,
            'created_by': self.created_by,
            'due_date': self.due_date
        }