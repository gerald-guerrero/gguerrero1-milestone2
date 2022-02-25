import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, UserMixin, login_user, current_user, logout_user
from dotenv import load_dotenv, find_dotenv
import os

app = flask.Flask(__name__)

load_dotenv(find_dotenv())
SECRET_KEY = os.getenv("SECRET_KEY")
app.config['SECRET_KEY'] = SECRET_KEY
uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.login_view = "account.login"
login_manager.init_app(app)

from models import Users, Comments, db
db.init_app(app)
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))



from account import account
app.register_blueprint(account)

from movies import movies
app.register_blueprint(movies)

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)