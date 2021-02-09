from flask import flash, redirect, render_template, request, url_for, Blueprint
from project import db
from project.users.utils import *
from project.users.forms import *

users_blueprint = Blueprint(
    'users', 
    __name__, 
    template_folder='templates'
)

# ---------------------VIEWS----------------------


@users_blueprint.route("/")  # routes user to this page depending on what page they put in
@users_blueprint.route("/home", endpoint="home")
def home():
    return render_template("home.html")


@users_blueprint.route("/terms")
def terms():
    return render_template("terms.html")


@users_blueprint.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form["submit_button"] == "existing_user":
            user = request.form["nm"]
            password = request.form["pw"]
            # session.permanent = True
            # session["user"] = user

            if find_user(user):
                if valid_user(find_user(user), password):
                    flash("Login Successful!")
                    return render_template("home.html")
                else:
                    flash("Username and/or password does not match")
                    return redirect(url_for("users.login"))
            elif valid_email(user) and valid_email(user).password == password:
                # session["email"] = found_user.email
                flash("Login Successful!")
                return render_template("home.html")
            else:
                flash("Username and/or password does not match")
                user = ""
                password = ""
                return redirect(url_for("users.login"))

        elif request.form["submit_button"] == "new_user":
            user = request.form["new_nm"]
            password = request.form["new_pw"]
            email = request.form["email"]
            usr = add_user(user, password, email)
            db.session.add(usr)
            db.session.commit()
            flash("Logged In Successfully!")
            return redirect(url_for("users.home"))

    else:
        return render_template("login.html")
    """
    else:
        if "user" in session:
            flash("Already Logged In!", "info")
            return redirect(url_for("home"))
        return render_template("login.html")
    """


@users_blueprint.route("/logout")
def logout():
    """
    if "user" in session:
        flash("Logged out succesfully", "info")
    else:
        flash("No user in session", "error")
    """
    clear_session(session_var)
    return redirect(url_for("users.login"))


@users_blueprint.route("/manage", methods=["POST", "GET"])
def manage():
    if request.method == "POST":
        user = request.form["user"]
        search_user.filter_by(name=user).delete()
        db.session.commit()
    return render_template("manage.html", values=search_user.all())
