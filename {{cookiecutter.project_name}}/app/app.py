from flask import Flask
from flask_restful import Api
from app.resources.user_resource import UserResource
from app.utils.config import Config
from app.models.user import db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db.init_app(app)

# Add resources
api.add_resource(UserResource, '/users')