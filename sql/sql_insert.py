import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()
	c.execute("create table numbers(num INT)")
	for _ in range(100):
		x = random.randint(0, 100)
		c.execute("Insert into numbers values("+str(x)+")")
	c.execute("select * from numbers")
	rows = c.fetchall()
	for r in rows:
		print(r[0]) 
