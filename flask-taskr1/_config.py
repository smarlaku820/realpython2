import os

# grab the folder where this script lives

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
# cross-site request forgery prevention, which makes the app more secure
WTF_CSRF_ENABLED = True
SECRET_KEY = '\xfb\xa0\xde\xb4\xe6\xd2\xf1\xa5\xbe\xfd\x8c\xea\xf8\x12'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

