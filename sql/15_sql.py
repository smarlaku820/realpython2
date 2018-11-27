import sqlite3


with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	
	c.execute("""select make, model, count(*) from orders
		     group by make, model""")

	rows = c.fetchall()
	
	for row in rows:
		print(row[0], row[1], row[2])
