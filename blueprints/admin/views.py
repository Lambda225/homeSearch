import os
import re
import datetime
from flask import Blueprint,render_template, url_for, request , redirect,session,Response,request
import flask_login
from wtforms import form
from blueprints import db
from blueprints.admin.form import Form_connexion,Form_maison,Form_photo,Form_agence
from blueprints.admin.models import Admin
from blueprints.user.models import Agence, Image, Maison
from werkzeug.utils import secure_filename
import shutil
from flask_login import login_user,login_required, current_user,logout_user

admin = Blueprint('admin',__name__,template_folder='templates/admin',static_folder='static')

#Connexiion pour super utilisateur

@admin.route('',methods = ['get','post'])
def connexion():
    form = Form_connexion()
    email= form.mail.data
    personne = Admin.query.filter_by(mail=email).first()
    if form.validate_on_submit() and form.password.data == personne.passworld :
        login_user(personne,remember=False)
        return redirect(url_for('admin.home'))
    return render_template('connexion.html',form=form)

#Deconnection 

@admin.route('/deconnection')
def deconnection():
    logout_user()
    return redirect(url_for('admin.connexion'))

#Acceuil de maison

@admin.route('/home')
@login_required
def home():
    maisons = Maison.query.order_by(Maison.id).all()
    maisons.reverse()
    return render_template('Acceuil.html', maisons=maisons)

#Detail de maison

@admin.route('/detail/<int:id>')
def detail(id):
    maison = Maison.query.get(id)
    print(maison.maison_image)
    form = Form_photo()
    return render_template('detail.html',maison=maison,form=form)

#Ajouter Maison

@admin.route('/ajout',methods=['GET','POST'])
def ajout():
    form = Form_maison()
    if form.validate_on_submit():
        maison = Maison()
        maison.titre = form.titre.data
        maison.longitude = form.longitude.data
        maison.lartitude = form.latitude.data
        basename = secure_filename(form.photo.data.filename)
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filenames = "_".join([suffix,basename])
        maison.photo = filenames
        db.session.add(maison)
        db.session.commit()
        os.makedirs('C:/Users/PARFAIT/Documents/HomeSearch/blueprints/admin/static/uploads/'+maison.titre)
        form.photo.data.save(f'blueprints/admin/static/uploads/{maison.titre}/{filenames}')
        return redirect(url_for('admin.home'))
    return render_template('AjoutMaison.html',form=form)

#Ajouter photo a maison

@admin.route('/ajoutphoto/<int:id>',methods=['POST'])
def ajoutphoto(id):
    form = Form_photo()
    if form.validate_on_submit():
        maison =Maison.query.get(id)
        basename = secure_filename(form.photo.data.filename)
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filenames = "_".join([suffix,basename])
        form.photo.data.save(f'blueprints/admin/static/uploads/{maison.titre}/{filenames}')
        image = Image()
        image.nom = filenames
        image.Maison_id = maison.id
        db.session.add(image)
        db.session.commit()
        return redirect(url_for('admin.detail',id=id))

#supprimer maison

@admin.route('/supprimermaison/<int:id>')
def supprimermaison(id):
    maison =Maison.query.get(id)
    for image in maison.maison_image:
        print(image.nom)
        os.remove(f'C:/Users/PARFAIT/Documents/HomeSearch/blueprints/admin/static/uploads/{maison.titre}/{image.nom}')
        db.session.delete(image)
        db.session.commit()
    os.remove(f'C:/Users/PARFAIT/Documents/HomeSearch/blueprints/admin/static/uploads/{maison.titre}/{maison.photo}')
    shutil.rmtree(f'C:/Users/PARFAIT/Documents/HomeSearch/blueprints/admin/static/uploads/{maison.titre}')
    db.session.delete(maison)
    db.session.commit()
    return redirect(url_for('admin.home'))


#supprimer photo d'une maison

@admin.route('/supprimerphoto/<int:image_id>/<int:maison_id>')
def supprimerphoto(image_id, maison_id):
    image =Image.query.get(image_id)
    maison =Maison.query.get(maison_id)
    os.remove(f'C:/Users/PARFAIT/Documents/HomeSearch/blueprints/admin/static/uploads/{maison.titre}/{image.nom}')
    db.session.delete(image)
    db.session.commit()
    return redirect(url_for('admin.detail',id=maison_id))

#Acceuil agence 

@admin.route('/listangence')
def listangence():
    agences = Agence.query.order_by(Agence.id).all()
    agences.reverse()
    return render_template('Agences.html',agences=agences)

#Ajouter agence

@admin.route('/ajoutagence',methods = ['get','post'])
def ajoutagence():
    form = Form_agence()
    if form.validate_on_submit():
        agence = Agence()
        agence.nom = form.nom.data
        agence.tel = form.tel.data
        agence.mail = form.mail.data
        agence.nonSite = form.nomSite.data
        agence.urlSite = form.urlSite.data
        basename = secure_filename(form.photo.data.filename)
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filenames = "_".join([suffix,basename])
        agence.photo = filenames
        db.session.add(agence)
        db.session.commit()
        os.makedirs('C:/Users/PARFAIT/Documents/HomeSearch/blueprints/admin/static/uploads/'+agence.mail)
        form.photo.data.save(f'blueprints/admin/static/uploads/{agence.mail}/{filenames}')
        return redirect(url_for('admin.listangence'))
    return render_template('ajoutagence.html',form=form)