from project import db
from project.models import testmodel

dbName = testmodel
search_user = db.session.query(dbName)
session_var = {"user", "email"}


def find_user(user):
    found_user = search_user.filter_by(name=user).all()
    return found_user

def valid_email(user):
    found_email = search_user.filter_by(email=user).first()
    return found_email

def valid_user(users, password):
    for user in users:
        if user.password == password:
            return True
    return False
