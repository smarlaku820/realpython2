import sqlite3


with sqlite3.connect("cars.db") as connection:
        c = connection.cursor()

        c.execute("""select inventory.make, inventory.model, inventory.quantity, s.orderQ from
                        inventory, (select make mk, model mo, count(*) orderQ from orders group by mk, mo) s
                     where inventory.model = s.mo
                  """)

        rows = c.fetchall()

        for r in rows:
                print(" " + r[0] + " " + r[1] + "  Quantity :" + str(r[2]) + " No of Orders Received:" + str(r[3]))
                print(" ")
