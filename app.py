import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, UserMixin, login_user, current_user, logout_user
from dotenv import load_dotenv, find_dotenv
import os
import requests
from TMDB import movie_data
from WIKI import wiki_data
import random

app = flask.Flask(__name__)

load_dotenv(find_dotenv())
SECRET_KEY = os.getenv("SECRET_KEY")
app.config['SECRET_KEY'] = SECRET_KEY
uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    movie_id = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)
db.create_all()

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.route('/login')
def login():
    return flask.render_template('login.html', url=flask.url_for("signup"))

@app.route('/login_form', methods=["GET", "POST"])
def login_form():
    if flask.request.method == "POST":
        input = flask.request.form.get("username")
        user = Users.query.filter_by(username=input).first()
        if user is None:
            flask.flash("Error: Username not found")
            return flask.redirect(flask.url_for("login"))
        login_user(user)
    return flask.redirect(flask.url_for("index"))

@app.route('/signup')
def signup():
    return flask.render_template("signup.html", url=flask.url_for("login"))

@app.route('/signup_form', methods=["GET", "POST"])
def signup_form():
    if flask.request.method == "POST":
        input = flask.request.form.get("username")
        user = Users.query.filter_by(username=input).first()
        if user is None:
            new_user = Users(username=input)
            db.session.add(new_user)
            db.session.commit()
            return flask.redirect(flask.url_for("login"))
    flask.flash("Error: Username not acceptable")
    return flask.redirect(flask.url_for("signup"))

@app.route('/logout')
def logout():
    print(1)
    logout_user()
    return flask.redirect(flask.url_for("login"))

@app.route("/")
@login_required
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
        logout=flask.url_for("logout"),
        comments=comments
    )
@app.route('/save', methods=["GET", "POST"])
def save():
    if flask.request.method == "POST":
        input = flask.request.form
        username = current_user.username
        movie_id = input.get("movie id")
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