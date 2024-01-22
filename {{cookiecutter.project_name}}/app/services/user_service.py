# app/services/user_service.py

from app.models.user import User
from app.app import db

class UserService:
    @staticmethod
    def get_all_users():
        """Get all users from the database."""
        return User.query.all()

    @staticmethod
    def create_user(username, email):
        """Create a new user and save it to the database."""
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_id(user_id):
        """Get a user by ID from the database."""
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id, new_username, new_email):
        """Update user information in the database."""
        user = User.query.get(user_id)
        if user:
            user.username = new_username
            user.email = new_email
            db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        """Delete a user from the database."""
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user
