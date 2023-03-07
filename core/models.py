from core import db

# define the Assignment model for the assignment tracker
class Assignment(db.Model):
    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.Date, nullable=False)
    category= db.Column(db.String, db.ForeignKey('category.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    user = db.relationship('User', backref='assignments')

    def __repr__(self):
        return '<Assignment {}>'.format(self.title)
