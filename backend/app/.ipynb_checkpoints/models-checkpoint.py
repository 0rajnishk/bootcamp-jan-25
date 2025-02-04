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
        return f'<User, {username}>'

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'role': self.role
        }

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.string(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.string(120), nullable=False, default="assigned")
    assigned_to = db.Column(db.Integer, db.Foreignkey(User.id),  nullable=False)


    def __repr__(self):
        return f'<Task, {title}>'

    def serialize(self):
        return {
            'title': self.title,
            'description': self.description,
            'role': self.role
        }