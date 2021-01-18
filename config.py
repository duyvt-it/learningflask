import os

class Config(object):
    """
    docstring
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6a0fd6c797c89927004896e5dc8f1ad6'