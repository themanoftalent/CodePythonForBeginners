import sqlite3
from employee import Employee



conn=sqlite3.connect('employee.db')
# conn=sqlite3.connect(':memory:') we can use memory

c=conn.cursor()

# c.execute("""CREATE TABLE employees(
# 				first text,
# 				last text,
# 				pay integer
# 				)""")


emp1=Employee('Sultan','Gokce',3455)
emp2=Employee('Ismail','Sert',5100)

# print(emp1.first)
# print(emp1.last)
# print(emp1.pay)

#normally we are going to use string format for insertion but this is open to sql injection
# c.execute("INSERT INTO employees VALUES ('{}','{}','{}')".format(emp1.first,emp1.last,emp1.pay))
#instaead we use
c.execute("INSERT INTO employees VALUES (?,?,?)",(emp1.first,emp1.last,emp1.pay))

conn.commit()
print(c.fetchall()) 

#or

c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':emp2.first,'last':emp2.last,'pay':emp2.pay})

conn.commit()


c.execute("INSERT INTO employees VALUES ('Akif','Kaya',4300)")


# c.execute("INSERT INTO employees VALUES ('Mahmut','Kaya',3100)")

# conn.commit()

# c.execute("SELECT * FROM employees WHERE first='Ismail' ")
c.execute("SELECT * FROM employees WHERE last=:last ",{'last':'Gokce'})

print(c.fetchmany(1)) 
conn.commit()

conn.close()