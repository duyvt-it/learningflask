import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    docstring
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6a0fd6c797c89927004896e5dc8f1ad6'

    # Config Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Config for email notification
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USENAME = os.environ.get('MAIL_USENAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['voduy987.tdv1@gmail.com']
