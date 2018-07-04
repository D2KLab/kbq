import os

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





