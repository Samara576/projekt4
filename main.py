import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO students (name) VALUES ('Нурлан')")
conn.commit()

for row in cursor.execute("SELECT * FROM students"):
    print(row)

conn.close()