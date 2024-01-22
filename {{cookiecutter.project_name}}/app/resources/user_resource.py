# app/resources/user_resource.py

from flask_restful import Resource
from app.models.user import User

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return {'users': [{'username': user.username, 'email': user.email} for user in users]}
