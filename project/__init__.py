# __init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# initialization
loginManager = LoginManager()
app = Flask(__name__)

# Flask Application configuration
app.secret_key = 'secretKey'
path = os.path.abspath( os.path.dirname(__file__) )
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(path, 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

loginManager.init_app(app)
loginManager.login_view = 'login'