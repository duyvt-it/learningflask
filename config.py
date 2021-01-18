import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    docstring
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6a0fd6c797c89927004896e5dc8f1ad6'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
