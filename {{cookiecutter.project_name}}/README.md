# {{cookiecutter.project_name}}

This is a simple Flask project for a REST API with user data.

## Getting Started

### Prerequisites

- Python 3.x
- [Virtualenv](https://virtualenv.pypa.io/)

### Installation

Create virtual env and install necessary requirements
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```


# {{cookiecutter.project_name}}
This is a simple Flask REST API project with models, services, and a main application.

# Project Structure
```
{{cookiecutter.project_name}}/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── app.py
├── tests/
│   ├── __init__.py
│   ├── resources/
│   │   ├── __init__.py
│   │   ├── test_user_resource.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── test_user_service.py
├── venv/ (virtual environment)
├── requirements.txt
```

# Components
## Models
The models directory contains SQLAlchemy models. In this example, there is a User model defined in app/models/user.py. This model represents a basic user with id, username, and email fields.

## Services
The services directory contains service classes that encapsulate business logic related to the models. The UserService in app/services/user_service.py provides CRUD operations for the User model.

## Main App
The main Flask application is defined in app.py. It configures the Flask app, sets up the database, and registers the API resources.

# How to Run
## Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Run the Flask app:
```
(venv) ➜  MyFlaskRestApp python run.py
 * Serving Flask app 'app.app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 135-691-727
```
The app will be accessible at http://127.0.0.1:5000/

## How to Test

### Activate the virtual environment (if not activated):

```
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Run the tests:
```
(venv) ➜  MyFlaskRestApp pytest tests/
======================================================= test session starts =======================================================
platform darwin -- Python 3.11.7, pytest-7.4.4, pluggy-1.3.0
rootdir: /MyFlaskRestApp
collected 2 items                                                                                                                 

tests/resources/test_user_resource.py .                                                                                     [ 50%]
tests/services/test_user_service.py .                                                                                       [100%]

======================================================== 2 passed in 0.38s ========================================================
```

This script will discover and run all test files in the tests directory.

---
This README provides a basic overview of the project structure, components, and instructions on how to run and test the Flask app. Customize it further based on your project's specific details and requirements.

