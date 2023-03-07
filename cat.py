from core.tracker.models import Category
from core import db, app 

#adding the status of assignments
app.app_context().push()

ctgry1 = Category(name='Not Started')
ctgry2 = Category(name='In Progress')
ctgry3 = Category(name='Completed')

with app.app_context():
  db.session.add(ctgry1)
  db.session.add(ctgry2)
  db.session.add(ctgry3)
  db.session.commit()

categories = Category.query.all()
for c in categories:
    print (c.name)  