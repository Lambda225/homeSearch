from datetime import time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,DateField,TextAreaField,FileField,form,IntegerField
from wtforms import validators,ValidationError
from blueprints.user.models import Utilisateur
from wtforms.validators import DataRequired,Email,EqualTo

class Form_commentaire_site(FlaskForm):
    contenu = TextAreaField('CONTENU',validators=[DataRequired()])
    submit = SubmitField('Envoyer')

class Form_connexion(FlaskForm):
    mail = StringField('MAIL',validators=[DataRequired(),Email()])
    password = PasswordField('MOTS DE PASSE',validators=[DataRequired()])
    submit = SubmitField('Envoyer')

    def validate_mail(self, mail):
        if not(Utilisateur.query.filter_by(mail=mail.data).first()):
            return ValidationError("Mail inexistant")

class Form_inscription(FlaskForm):
    nom = StringField('Nom',validators=[DataRequired()])
    prenom = StringField('Prenom',validators=[DataRequired()])
    mail = StringField('MAIL',validators=[DataRequired(),Email()])
    tel = StringField('Tel',validators=[DataRequired()])
    password = PasswordField('MOTS DE PASSE',validators=[DataRequired()]) 
    confirm_password = PasswordField('Confirmer Mots De Passe',validators=[DataRequired()])
    submit = SubmitField('Envoyer') 