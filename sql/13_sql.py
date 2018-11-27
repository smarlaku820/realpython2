import sqlite3
with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	c.execute("SELECT inventory.make, inventory.model, inventory.quantity, orders.order_date  FROM inventory, orders where orders.model = inventory.model ORDER BY inventory.make ASC")
	rows = c.fetchall()
	for r in rows:
		print("Cars Make :" + r[0] + "Cars Model :" + r[1])
		print("Cars Quantity :" + str(r[2]))
		print("Cars Order Date :" + str(r[3]))
		print(" ")
