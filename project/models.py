from project import db

class testmodel(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
