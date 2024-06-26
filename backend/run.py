

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from config import SECRET_KEY, TEMPLATES_PATH

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['TEMPLATES_FOLDER'] = TEMPLATES_PATH

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.run('127.0.0.1', 5000)
