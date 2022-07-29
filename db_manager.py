import sqlite3

conn = sqlite3.connect('lakes.db')

c = conn.cursor()
# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#             )""")

# c.execute("INSERT INTO employees VALUES ('Corey', 'Wilkinson', 20000)")

c.execute("SELECT * FROM employees WHERE last='Wilkinson'")
print(c.fetchone())

# commits changes to database
conn.commit()

# closes connection to database
conn.close()