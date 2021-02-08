from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "supersecret123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3?check_same_thread=False'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.permanent_session_lifetime = timedelta(minutes=5)


db = SQLAlchemy(app)

class testmodel(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

dbName = testmodel
search_user = db.session.query(dbName)


def add_user(name, password, email):
    return dbName(name, password, email)


session_var = {"user", "email"}


def clear_session(session_var):
    for data in session_var:
        session.pop(data, None)


@app.route("/")  # routes user to this page depending on what page they put in
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form["submit_button"] == "existing_user":
            # session.permanent = True
            user = request.form["nm"]
            # session["user"] = user
            password = request.form["pw"]

            found_user = search_user.filter_by(name=user).all()
    
            if found_user:
                for person in found_user:
                    if person.password == password:
                        # session["email"] = found_user.email
                        flash("Login Successful!")
                        return render_template("home.html")
                else:
                    flash("Username and/or password does not match")
                    user = ""
                    password = ""
                    return redirect(url_for("login"))
            else:
                flash("Username and/or password does not match")
                return redirect(url_for("login"))
        elif request.form["submit_button"] == "new_user":
            user = request.form["new_nm"]
            password = request.form["new_pw"]
            email = request.form["email"]
            usr = add_user(user, password, email)
            db.session.add(usr)
            db.session.commit()
            flash("Logged In Successfully!")
            return redirect(url_for("home"))
    else:
        return render_template("login.html")
    """
    else:
        if "user" in session:
            flash("Already Logged In!", "info")
            return redirect(url_for("home"))
        return render_template("login.html")
    """

@app.route("/logout")
def logout():
    """
    if "user" in session:
        flash("Logged out succesfully", "info")
    else:
        flash("No user in session", "error")
    """
    clear_session(session_var)
    return redirect(url_for("login"))


@app.route("/view", methods=["POST", "GET"])
def view():
    if request.method == "POST":
        user = request.form["user"]
        search_user.filter_by(name=user).delete()
        db.session.commit()
    return render_template("view.html", values=search_user.all())


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
