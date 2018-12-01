from views import db
from models import Task
from datetime import date


db.create_all()
db.session.add(Task("Finish this tutorial", date(2018, 12, 31), 10, 1))
db.session.add(Task("Finish Real Python 2", date(2019, 1, 31), 10, 1))
db.session.commit()
	
