from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
# from flask_login import UserMixin

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")
    subscriptions = db.relationship('Subscription', backref = 'user', lazy = "dynamic")

    def __repr__(self):
        return f'User {self.username}'

class Writer(db.Model):
    __tablename__ = 'writers'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String)
    pass_secure = db.Column(db.String(255))
    posts = db.relationship('Post', backref = 'writer', lazy = "dynamic")
    comments = db.relationship('Comment', backref = 'writer', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    time_posted = db.Column(db.DateTime)
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    comments = db.relationship('Comment', backref = 'writer', lazy = "dynamic")

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String)
    time_posted = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))

class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    