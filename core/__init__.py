from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# configure the login manager
auth_login_manager = LoginManager(app)
auth_login_manager.login_view = 'auth.login'

# define the assignment tracker blueprint
from .tracker.views import assignment_tracker_blueprint
app.register_blueprint(assignment_tracker_blueprint)

# define the authentication blueprint
from .auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)

from core import views, models