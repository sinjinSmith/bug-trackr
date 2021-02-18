from flask import Flask, Blueprint, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, send

# app.permanent_session_lifetime = timedelta(minutes=5)
app = Flask(__name__)
app.secret_key = "supersecret123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3?check_same_thread=False'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

socketio = SocketIO(app)
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.chatroom.views import chatroom_blueprint

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(chatroom_blueprint, url_prefix="/chatroom")

@app.route('/')
def root():
    return redirect(url_for('users.login'))
