import sqlite3

def create_db():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("create table posts(title text, content text, author text, blog_id integer)")
    c.execute("create table comments(content text, blog integer, author text)")
    conn.commit()
    conn.close()
    
def add_blog(name):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    command = "INSERT INTO blogs VALUES(" + name + ")"
    c.execute(command)
    conn.commit()
    conn.close()
    
def blog_list():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    cur = c.execute("SELECT name FROM blogs")
    blogs = []
    for blog in cur:
        print blog
        blogs.append(blog)
    return blogs
