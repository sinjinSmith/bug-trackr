from project import db
from project.models import testmodel
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash

dbName = testmodel
search_user = db.session.query(dbName)
session_var = {"user", "email"}

# def clear_all_data():
#     db.session.query(dbName).delete()
#     db.session.commit()

def add_user(name, password, email):
    return dbName(
        name, 
        generate_password_hash(password, method='pbkdf2:sha256', salt_length=8),
        email
    )

def clear_session(session_var):
    for data in session_var:
        session.pop(data, None)

def find_user(user):
    found_user = search_user.filter_by(name=user).all()
    return found_user

def valid_email(user):
    found_email = search_user.filter_by(email=user).first()
    return found_email

def valid_user(users, password):
    for user in users:
        if check_password_hash(user.password, password):
            return True
    return False
