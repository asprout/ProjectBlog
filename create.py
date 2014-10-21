import sqlite3

conn = sqlite3.connect("blog.db")
c = conn.cursor()

def create_tables():
    c.execute("create table blogs(name text)")
    c.execute("create table posts(title text, content text, author text, blog_id integer)")
    c.execute("create table comments(content text, blog integer, author text)")
