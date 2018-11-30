from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,unique=True)
    password = db.Column(db.String)
    email = db.Column(db.String,unique=True)

    def __init__(self,name=None,email=None,password=None):
        self.name = name
        self.email = email
        self.password = password

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String,unique=True)
    author = db.Column(db.String)
    year = db.Column(db.Integer)
    isbn = db.Column(db.String)
    review_count = db.Column(db.Integer)
    average_score = db.Column(db.Float)

    def __init__(self,title=None,author=None,year=None,isbn=None):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer,primary_key=True)
    score = db.Column(db.Integer)
    description = db.Column(db.String)
    id_book = db.Column(db.Integer, db.ForeignKey('books.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self,score=None,description=None):
        self.score = score
        self.description = description
