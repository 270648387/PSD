import sqlite3

# Create an in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("CREATE TABLE test (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO test VALUES (1, 'Hello')")
cursor.execute("SELECT * FROM test")

print(cursor.fetchall())  # should print [(1, 'Hello')]

conn.close()
