import os 
from flask import Flask
from flask_login.utils import login_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Definition de chemin vers le app.py
basedire = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blablayzcyzq'

#configue de la base de donnée
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedire,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#Instanciation de SQLALCHEMY
db = SQLAlchemy(app)
Migrate(app, db)

from blueprints.user.models import Utilisateur
from blueprints.admin.models import Admin

#initialisation des blueprints
from blueprints.user.views import user
from blueprints.admin.views import admin

app.register_blueprint(admin,url_prefix='/admin/')
app.register_blueprint(user,url_prefix='/user/')

#Instancition du flas_login
login_manager = LoginManager()
login_manager.login_view = 'admin.connexion'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))