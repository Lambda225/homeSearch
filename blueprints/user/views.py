import os
import re
import datetime
from flask import Blueprint,render_template, url_for, request , redirect,session,Response,request
from wtforms import form
from blueprints import db
from blueprints.user.models import Maison,Commentaire_site,Utilisateur
from blueprints.user.form import Form_commentaire_site,Form_connexion,Form_inscription
from werkzeug.utils import secure_filename

user = Blueprint('user',__name__,template_folder='templates/user',static_folder='static')

#fonction qui retourne le premier prenom
def AvoirPrenom(user):
    listeprenom= user.prenom.split()
    return listeprenom[0].upper()


#Acceuil pour utilisateur
@user.route('')
def home():
    maisons = Maison.query.order_by(Maison.id).limit(3).all()
    commentaires = Commentaire_site.query.order_by(Commentaire_site.id).all()
    form = Form_commentaire_site()
    return render_template('Acceuil.htm',maisons=maisons,commentaires=commentaires,form=form)

#Liste de toutes les maisons disponibles
@user.route('/maisons')
def maisons():
    maisons = Maison.query.order_by(Maison.id).all()
    form = Form_commentaire_site()
    return render_template('Maison.html',maisons=maisons,form=form)

#Contact du site
@user.route('/contact')
def contact():
    return render_template('contact.html')

#Consulter detail de maison
@user.route('/detail/<int:id>')
def detail(id):
    maison = Maison.query.get(id)
    maisons = Maison.query.order_by(Maison.id).all()
    form = Form_commentaire_site()
    return render_template('Detailmaison.html', maison=maison,form=form,maisons=maisons)

#Visite 3d
@user.route('/vue/<int:id>')
def vue(id):
    maison = Maison.query.get(id)
    return render_template('view.html',maison=maison)

#connection
@user.route('/connection',methods = ['get','post'])
def connection():
    form = Form_connexion()
    email= form.mail.data
    personne = Utilisateur.query.filter_by(mail=email).first()
    if form.validate_on_submit() and form.password.data == personne.password :
        preprenom = AvoirPrenom(personne)
        session['user'] = {
                'id':personne.id,
                'nom':personne.nom,
                'prenom':preprenom,
            }
        return redirect(url_for('user.home'))
    return render_template('connection.html',form=form)


#Inscription
@user.route('/inscription',methods = ['get','post'])
def inscription():
    form = Form_inscription()
    if form.validate_on_submit():
        personne  = Utilisateur()
        personne.mail = form.mail.data
        personne.tel = int(form.tel.data)
        personne.nom = form.nom.data
        personne.prenom = form.prenom.data
        personne.password = form.password.data
        db.session.add(personne)
        db.session.commit()
        preprenom = AvoirPrenom(personne)
        session['user'] = {
                'id':personne.id,
                'nom':personne.nom,
                'prenom':preprenom,
            }
        return redirect(url_for('user.home'))
    return render_template('Inscription.html',form=form)

#route de profile
@user.route('/profile')
def profile():
    try:
        print(session['user'])
    except:
        return redirect(url_for('user.connection'))
    user = Utilisateur.query.get(session['user']['id'])
    return render_template('profile.html',user = user)


#route de deconnection
@user.route('deconnection')
def deconnection():
    del session['user']
    return redirect(url_for('user.home'))

#route pour contacter le site
@user.route('/envoi',methods = ['post'])
def envoi():
    try:
        print(session['user'])
    except:
        return redirect(url_for('user.connection'))
    form = Form_commentaire_site()
    if form.validate_on_submit():
        commentaire=Commentaire_site()
        commentaire.contenue = form.contenu.data
        commentaire.Utilisateur_id = session['user']['id']
        db.session.add(commentaire)
        db.session.commit()
        return redirect(url_for('user.home'))
