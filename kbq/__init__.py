from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from kbq.config import Config

mongo = PyMongo()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from kbq.rest.routes import rest
    #from kbq.sparql.routes import sparql
    from kbq.webapp.routes import webapp
    
    app.register_blueprint(rest)
    #app.register_blueprint(sparql)
    app.register_blueprint(webapp)

    return app



