import flask
from flask_login import login_user
from models import Users, db

# pylint: disable=no-member

account = flask.Blueprint("account", __name__)


@account.route("/login")
def login():
    return flask.render_template("login.html", url=flask.url_for("account.signup"))


@account.route("/login_form", methods=["GET", "POST"])
def login_form():
    if flask.request.method == "POST":
        input = flask.request.form.get("username")
        user = Users.query.filter_by(username=input).first()
        if user is None:
            flask.flash("Error: Username not found")
            return flask.redirect(flask.url_for("account.login"))
        login_user(user)
    return flask.redirect(flask.url_for("movies.index"))


@account.route("/signup")
def signup():
    return flask.render_template("signup.html", url=flask.url_for("account.login"))


@account.route("/signup_form", methods=["GET", "POST"])
def signup_form():
    if flask.request.method == "POST":
        input = flask.request.form.get("username")
        user = Users.query.filter_by(username=input).first()
        if user is None:
            new_user = Users(username=input)
            db.session.add(new_user)
            db.session.commit()
            return flask.redirect(flask.url_for("account.login"))
    flask.flash("Error: Username not acceptable")
    return flask.redirect(flask.url_for("account.signup"))
