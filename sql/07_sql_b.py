import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	try:
		c.execute("select * from inventory where make='Ford'")
		rows = c.fetchall()
		for r in rows:
			print(r[0], r[1], r[2])
	except sqlite3.OperationalError:
		print("something went wrong, please review!!")
