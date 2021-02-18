from flask import flash, redirect, render_template, request, url_for, Blueprint
from project import db
from project.users.forms import *

chatroom_blueprint = Blueprint(
    'chatroom',
    __name__,
    template_folder='templates'
)

# ---------------------VIEWS----------------------

@chatroom_blueprint.route("/")
def home():
    return render_template("chat.html")