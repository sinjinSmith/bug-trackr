from main import dbName
from flask import session

def add_user(name, password, email):
    return dbName(name, password, email)

def clear_session(session_var):
    for data in session_var:
        session.pop(data, None)
