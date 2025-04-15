import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:RtUv9929@localhost/newdatabaseee'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
