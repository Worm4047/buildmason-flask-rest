# tests/services/test_user_service.py

import unittest
from unittest.mock import patch
from app.services.user_service import UserService
from app.models.user import User, db
from app.app import app

class TestUserService(unittest.TestCase):
    def setUp(self):
        # Configure the Flask app for testing
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

        # Create the database tables
        db.create_all()

        # Insert sample data into the database
        self.user1 = User(username='user1', email='user1@example.com')
        self.user2 = User(username='user2', email='user2@example.com')
        db.session.add_all([self.user1, self.user2])
        db.session.commit()

    def tearDown(self):
        # Remove the database tables and close the app context
        db.drop_all()
        self.app_context.pop()

    def test_get_all_users(self):
        # Assuming UserService.get_all_users() fetches all users from the database
        with patch('app.services.user_service.User.query') as mock_query:
            mock_query.all.return_value = [self.user1, self.user2]
            users = UserService.get_all_users()
            self.assertEqual(len(users), 2)
            self.assertEqual(users[0].username, 'user1')
            self.assertEqual(users[1].username, 'user2')

    # Add more test cases for other methods in UserService

if __name__ == '__main__':
    unittest.main()
