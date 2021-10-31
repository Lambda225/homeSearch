from blueprints import db
from flask_login import UserMixin

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.Text)
    nom = db.Column(db.Text)
    prenom = db.Column(db.Text)
    passworld = db.Column(db.Text)

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.nom)