from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from kbq.config import Config
from flask_apscheduler import APScheduler

mongo = PyMongo()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


import time
import schedule
from kbq.schdeduler.apiScheduler import scheduler_module


def create_app(config_class = Config):

    """Factory Method"""

    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    mongo.app = app
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    from kbq.rest.routes import rest
    from kbq.webapp.routes import webapp
    from kbq.metrics.metrics import metrics
    from kbq.schdeduler.apiScheduler import schedule
        
    app.register_blueprint(rest)
    app.register_blueprint(metrics)
    app.register_blueprint(webapp)
    app.register_blueprint(schedule)

    scheduler  = APScheduler()
    scheduler.init_app(app)
    scheduler.add_job(func=scheduler_module,id='1',trigger='interval',hours=4,replace_existing=True)
    #scheduler.add_job(scheduler_module, trigger='interval', seconds=3)
    scheduler.start()
        
    return app




