import sqlite3


def create_db():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("create table blogs(name text)")
    c.execute("create table posts(title text, content text, author text, blog_id integer)")
    c.execute("create table comments(content text, blog integer, author text)")
    conn.commit()
    
def add_blog(name):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("INSERT INTO blogs VALUES('%(name)s')")
    conn.commit()
