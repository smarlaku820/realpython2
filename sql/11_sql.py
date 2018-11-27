# JOINing data from multiple tables
import sqlite3
with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
# retrieve data
	c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")
	c.execute("SELECT * FROM INVENTORY")
	rows = c.fetchall()
	for r in rows:
		print(r[0], r[1], r[2])
