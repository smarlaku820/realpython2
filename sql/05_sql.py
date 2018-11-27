import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	employees = csv.reader(open("employees.csv", "r"))
	c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
	c.executemany("Insert into employees(firstname, lastname) values(?, ?)", employees)
