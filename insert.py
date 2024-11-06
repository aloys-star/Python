import sqlite3

conn = sqlite3.connect('employee.db')
print("successfully connected to database")

conn.execute("INSERT INTO Employee VALUES(1,'Mark','Mugo',43,230000.00,'Manager')")
conn.execute("INSERT INTO Employee VALUES(2,'Rose','Maina',40,200000.00,'Assistant Manager')")
conn.execute("INSERT INTO Employee VALUES(3,'James','Kiptoo',32,180000.00,'Secretary')")
conn.execute("INSERT INTO Employee VALUES(4,'Grace','Wambui',38,200000.00,'HR')")
conn.execute("INSERT INTO Employee VALUES(5,'Roy','Kiplagat',34,160000.00,'Admin')")
conn.execute("INSERT INTO Employee VALUES(6,'Martin','Odhiambo',32,150000.00,'Cosultant')")

conn.commit()
print("successfully inserted values into Employee table")