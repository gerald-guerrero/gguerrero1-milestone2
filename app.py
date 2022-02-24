import flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
import os

from sqlalchemy import true
from TMDB import movie_data
from WIKI import wiki_data
import random

app = flask.Flask(__name__)
load_dotenv(find_dotenv())

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    movie_id = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(750))
db.create_all()

@app.route("/")
def index():
    id_list = []
    id_list.append(1891)
    id_list.append(604)
    id_list.append(155)

    movie_id = random.choice(id_list)
    title, tagline, genres, image = movie_data(movie_id)
    url = wiki_data(title)

    comments = []
    comments = Comments.query.filter_by(movie_id=movie_id).all()
 
    
    return flask.render_template(
        "index.html",
        movie_id=movie_id,
        title=title,
        tagline=tagline,
        genres=genres,
        image=image,
        url=url,
        comments=comments
    )
@app.route('/save', methods=["GET", "POST"])
def save():
    if flask.request.method == "POST":
        input = flask.request.form
        username = "Guest"
        movie_id = input.get("movie id")
        print(movie_id)
        rating = int(input.get("rating"))
        comment = input.get("comment")

        new_comment = Comments(username=username, movie_id=movie_id, rating=rating, comment=comment)
        db.session.add(new_comment)
        db.session.commit()
    return flask.redirect(flask.url_for("index"))

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)