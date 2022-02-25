from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import flask

# pylint: disable=no-member

models = flask.Flask(__name__)

db = SQLAlchemy()


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    movie_id = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)
