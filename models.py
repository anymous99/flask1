from database import db
from sqlalchemy.orm import relationship


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)

    speakingTest = relationship(
        'SpeakingTest', back_populates='user', cascade='all,delete,delete-orphan')
    listeningTest = relationship(
        'ListeningTest', back_populates='user', cascade='all,delete,delete-orphan')

    def __repr__(self):
        return f"<User {self.name}>"


class SpeakingTest(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question = db.Column(db.String(200), nullable=False)
    response = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    user = relationship('User', back_populates='speakingTest')


class ListeningTest(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question = db.Column(db.String(200), nullable=False)
    response = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    user = relationship('User', back_populates='listeningTest')
