
from project.models import testmodel
from flask import session

def add_user(name, password, email):
    return testmodel(name, password, email)

def clear_session(session_var):
    for data in session_var:
        session.pop(data, None)
