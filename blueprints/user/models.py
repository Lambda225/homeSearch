from blueprints import db

commantaire_maison = db.Table('user_like',
    db.Column('utilisateur_id', db.Integer, db.ForeignKey('utilisateur.id')),
    db.Column('commentaire_maison_id', db.Integer, db.ForeignKey('commentaire_maison.id'))
) 

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20))
    prenom = db.Column(db.String(70))
    mail = db.Column(db.Text)
    tel = db.Column(db.Integer)
    password = db.Column(db.Text)
    photo = db.Column(db.Text) 
    utilisateur_commentaire = db.relationship("Commentaire_site",uselist=True)

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.nom)

class Agence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20))
    photo = db.Column(db.Text) 
    tel = db.Column(db.Text)
    mail = db.Column(db.Text)
    nonSite = db.Column(db.Text)
    urlSite = db.Column(db.Text)
    agence_maison = db.relationship("Maison",uselist=True)

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.nom)

class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.Text)
    categirie_maison = db.relationship("Maison",uselist=True)

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.titre)

class Maison(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.Text)
    photo = db.Column(db.Text)
    description = db.Column(db.Text)
    longitude = db.Column(db.Integer)
    lartitude = db.Column(db.Integer)
    prix = db.Column(db.Text)
    Agence_id = db.Column(db.Integer, db.ForeignKey('agence.id'))
    Categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'))
    maison_image = db.relationship("Image",uselist=True)
    maison_categorie = db.relationship("Categorie",uselist=True)

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.titre)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.Text)
    Maison_id = db.Column(db.Integer, db.ForeignKey('maison.id'))
    image_maison = db.relationship("Maison",uselist=True)

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.nom)

class Commentaire_site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenue = db.Column(db.Text)
    Utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.id)

class Commentaire_maison(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenue = db.Column(db.Text)
    Utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))
    like = db.relationship('Utilisateur', secondary=commantaire_maison, lazy='subquery',backref=db.backref('commentaire_maison', lazy='dynamic'))
    

    def __init__(self):
        pass

    def __repr__(self):
        return str(self.id)

