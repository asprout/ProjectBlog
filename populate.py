import sqlite3

conn = sqlite3.connect("blog.db")
c = conn.cursor()

def add_blog(name):
    c.execute("INSERT INTO blogs VALUES(%name)")
    conn.commit()
