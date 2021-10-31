from datetime import time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,DateField,TextAreaField,FileField,form,IntegerField
from wtforms import validators,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo
from blueprints.admin.models import Admin
from blueprints.user.models import Maison


class Form_connexion(FlaskForm):
    mail = StringField('MAIL',validators=[DataRequired(),Email()])
    password = PasswordField('MOTS DE PASSE',validators=[DataRequired()])
    submit = SubmitField('Envoyer')

    def validate_mail(self, mail):
        if not(Admin.query.filter_by(mail=mail.data).first()):
            return ValidationError("Mail inexistant")

class Form_maison(FlaskForm):
    titre = StringField('Titre',validators=[DataRequired()])
    photo = FileField('PHOTO',validators=[DataRequired()])
    longitude = IntegerField('Longitude',validators=[DataRequired()])
    latitude = IntegerField('Latitude',validators=[DataRequired()])
    submit = SubmitField('Envoyer')

    def validate_titre(self, titre):
        if not(Maison.query.filter_by(titre=titre.data).first()):
            return ValidationError("Mail inexistant")

class Form_photo(FlaskForm):
    photo = FileField('PHOTO',validators=[DataRequired()])
    submit = SubmitField('Envoyer')

class Form_agence(FlaskForm):
    nom = StringField('Nom',validators=[DataRequired()])
    photo = FileField('PHOTO',validators=[DataRequired()])
    tel = StringField('TEL',validators=[DataRequired()])
    mail = StringField('MAIL',validators=[DataRequired(),Email()])
    nomSite = StringField('NOM DE SITE',validators=[DataRequired()])
    urlSite = StringField('URL DE SITE',validators=[DataRequired()])
    submit = SubmitField('Envoyer')