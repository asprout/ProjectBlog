import sqlite3

conn = sqlite3.connect("blog.db")

c = conn.cursor()

c.execute("INSERT INTO blogs VALUES('Test Blog')")

conn.commit()
