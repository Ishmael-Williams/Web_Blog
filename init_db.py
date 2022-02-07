import sqlite3

Connection = sqlite3.Connection('database.db')
with open('schema.sql') as f:
	Connection.executescript(f.read())

cur = Connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?,?)",
		('First Post', 'Content for the first post')
		)

cur.execute("INSERT INTO posts (title, content) VALUES (?,?)",
		('Second Post', 'Content for the second post')
		)

Connection.commit()
Connection.close()

