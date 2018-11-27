import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()
	Inp = ["AVG", "SUM", "MAX", "MIN"]
	while True:
		uinp = raw_input("You may choose to Compute AVG/SUM/MAX/MIN: ")
		print(uinp)
		if uinp.upper() in Inp:
			break;
		else:
			print("Thats a Wrong Input!")
	
	sql_dict = { 'AVG' : 'select avg(num) from numbers',
		     'SUM' : 'select sum(num) from numbers',
		     'MAX' : 'select max(num) from numbers',
		     'MIN' : 'select min(num) from numbers'
		   }
	
	c.execute(sql_dict[uinp.upper()])
	row = c.fetchone()
	print("The "+uinp+" is calculated as "+str(row[0]))
