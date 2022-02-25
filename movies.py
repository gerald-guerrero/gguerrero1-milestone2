import flask
from flask_login import (
    login_required,
    current_user,
    logout_user,
)
from models import Comments, db
from TMDB import movie_data
from WIKI import wiki_data
import random

# pylint: disable=no-member

movies = flask.Blueprint("movies", __name__)


@movies.route("/logout")
def logout():
    logout_user()
    return flask.redirect(flask.url_for("account.login"))


@movies.route("/")
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
        logout=flask.url_for("movies.logout"),
        comments=comments,
    )


@movies.route("/save", methods=["GET", "POST"])
def save():
    if flask.request.method == "POST":
        input = flask.request.form
        username = current_user.username
        movie_id = input.get("movie id")
        rating = int(input.get("rating"))
        comment = input.get("comment")

        new_comment = Comments(
            username=username, movie_id=movie_id, rating=rating, comment=comment
        )
        db.session.add(new_comment)
        db.session.commit()
    return flask.redirect(flask.url_for("movies.index"))
