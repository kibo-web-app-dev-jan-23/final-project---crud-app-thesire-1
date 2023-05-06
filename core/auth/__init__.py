from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth',template_folder='templates')