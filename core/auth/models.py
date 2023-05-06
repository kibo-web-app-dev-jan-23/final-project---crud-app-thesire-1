from .. import db, auth_login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# define the User model for authentication
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# callback to reload the user object for authentication
@auth_login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))