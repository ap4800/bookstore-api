from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    published_date = db.Column(db.String(10))
    isbn = db.Column(db.String(13), unique=True)
    pages = db.Column(db.Integer)
    cover = db.Column(db.String(200))
    language = db.Column(db.String(2))
