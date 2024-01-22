# tests/resources/test_user_resource.py

import unittest
from app.models.user import User, db
from app.app import app

class TestUserResource(unittest.TestCase):
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

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()

        # Assuming the actual data structure returned by your API
        expected_data = {
            'users': [
                {'username': 'user1', 'email': 'user1@example.com'},
                {'username': 'user2', 'email': 'user2@example.com'}
            ]
        }

        self.assertEqual(data, expected_data)

if __name__ == '__main__':
    unittest.main()
