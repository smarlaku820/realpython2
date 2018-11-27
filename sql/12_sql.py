import sqlite3
with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	orders = [ ('Ford', 'Endeavor', 1988-05-11),
		   ('Ford', 'Endeavor', 1989-05-11),
		   ('Ford', 'Endeavor', 1999-06-11),
		   ('Ford', 'Ecosport', 1988-05-11),
		   ('Ford', 'Ecosport', 1989-05-11),
		   ('Ford', 'Ecosport', 1999-06-11),
		   ('Ford', 'Figo', 1988-05-11),
		   ('Ford', 'Figo', 1989-05-11),
		   ('Ford', 'Figo', 1999-06-11),
		   ('Honda', 'Civic', 1988-05-11),
		   ('Honda', 'Civic', 1989-05-11),
		   ('Honda', 'Civic', 1999-06-11),
		   ('Honda', 'Jazz', 1988-05-11),
		   ('Honda', 'Jazz', 1989-05-11),
		   ('Honda', 'Jazz', 1999-06-11),
		   ('Honda', 'City', 1988-05-11),
		   ('Honda', 'City', 1989-05-11),
		   ('Honda', 'City', 1999-06-11)
		]
	c.executemany("INSERT INTO orders values(?, ?, ?)", orders)
	c.execute("SELECT * FROM orders")
	rows = c.fetchall()
	for r in rows:
		print(r[0], r[1], r[2])
