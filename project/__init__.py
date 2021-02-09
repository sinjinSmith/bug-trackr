from flask import Flask, Blueprint, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

# app.permanent_session_lifetime = timedelta(minutes=5)
app = Flask(__name__)
app.secret_key = "supersecret123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3?check_same_thread=False'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from project.users.views import users_blueprint

app.register_blueprint(users_blueprint, url_prefix="/users")

@app.route('/')
def root():
    return redirect(url_for('users.login'))