from flask import Blueprint

assignment_tracker_blueprint = Blueprint('assignment_tracker', __name__, url_prefix='/assignment_tracker',template_folder='templates')