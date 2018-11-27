import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	cars = [
		('Ford', 'Endeavor', 5),
		('Ford', 'Ecosport', 2),
		('Ford', 'Figo', 10),
		('Honda', 'Civic', 3),
		('Honda', 'Jazz', 4),
		('Honda', 'City', 5)
		]
	try:
		c.executemany("Insert into inventory values(?, ?, ?)", cars)
	except sqlite3.OperationalError:
		print("something went wrong, please review!!")
