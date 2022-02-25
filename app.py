import flask
from flask_login import LoginManager
from dotenv import load_dotenv, find_dotenv
import os
from models import Users, db
from account import account
from movies import movies

# pylint: disable=no-member

app = flask.Flask(__name__)

load_dotenv(find_dotenv())
SECRET_KEY = os.getenv("SECRET_KEY")
app.config["SECRET_KEY"] = SECRET_KEY
uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

login_manager = LoginManager()
login_manager.login_view = "account.login"
login_manager.init_app(app)


db.init_app(app)
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


app.register_blueprint(account)

app.register_blueprint(movies)

app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
