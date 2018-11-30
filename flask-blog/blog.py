from flask import Flask, render_template, request, session, flash, redirect, url_for, g
from functools import wraps
import sqlite3

DATABASE = 'blog.db'
SECRET_KEY = '\xb7\x1c\xd7\x12\x14o\x8a\xe35\x17\xe5\\\xf5\xec\x00\xe7'
USERNAME='admin'
PASSWORD='admin'

app = Flask(__name__)

# pulls in app configuration by looking for upper case variables.

app.config.from_object(__name__)

# function used for connecting to the database

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])


@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	status_code = 200
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again.'
			status_code = 401
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html', error=error), status_code

# Python functools replicate existing functions with some arguments already passed in. It also creates new version of the function in a well-documented manner
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap


@app.route('/main')
@login_required
def main():
	g.db = connect_db()
	c = g.db.cursor()
	c.execute('select * from posts')
	posts = [dict(title=row[0], post=row[1]) for row in c.fetchall()]
	g.db.close()
	return render_template('main.html', posts=posts)


@app.route('/add', methods=['POST'])
@login_required
def add():
	title = request.form['title']
	post = request.form['post']
	if not title or not post:
		flash("All fields are required. Please try again")
		return redirect(url_for('main'))
	else:
		g.db = connect_db()
		c = g.db.cursor()
		c.execute('insert into posts (title, post) values (?, ?)', [request.form['title'], request.form['post']])
		g.db.commit()
		g.db.close()
		flash('New entry was successfully posted')
		return redirect(url_for('main'))


@app.route('/logout')
def logout():
        session.pop('logged_in', None)
        flash('You were logged out')
        return redirect(url_for('login'))


if __name__ == '__main__':
	app.run(debug=True)
