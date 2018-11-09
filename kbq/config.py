import os
from apscheduler.jobstores.mongodb import MongoDBJobStore


class Config:
    MONGO_DBNAME = 'kbq'
    # mLab mongo link
    #MONGO_URI = 'mongodb://rifat:abir963@ds119651.mlab.com:19651/kbq'
    # Local mongodb
    MONGO_URI = 'mongodb://localhost:27017/kbq'
    SECRET_KEY="powerful secretkey"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    #JINJA_ENVIRONMENT.globals['STATIC_PREFIX'] = '/'
    #APPLICATION_ROOT = '/KBQ'

    JOBS = []
    #SCHEDULER_JOBSTORES = {
    #    'default': MongoDBJobStore(host=MONGO_URI)
    #}
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }
    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 20
    }
    SCHEDULER_API_ENABLED = True






