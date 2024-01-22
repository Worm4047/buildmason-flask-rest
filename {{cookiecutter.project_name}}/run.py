# app/app.py

from flask import render_template
from app.app import app
from app.services.user_service import UserService

from app.models.user import db

# Check if tables exist, if not, create them
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Create users and save them to the database
    user1 = UserService.create_user(username='user1', email='user1@example.com')
    user2 = UserService.create_user(username='user2', email='user2@example.com')

    # Retrieve all users from the database
    users = UserService.get_all_users()

    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
