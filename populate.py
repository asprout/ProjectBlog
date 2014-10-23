import sqlite3

def create_db():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("create table blog (name text, blog_id integer)")
    c.execute("create table posts(title text, content text, author text, blog_id integer, post_id integer)")
    c.execute("create table comments(content text, post_id integer, author text)")
    conn.commit()
    conn.close()
    
def add_blog(name):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    currentMax = c.execute("select max(blog_id) from blog").fetchone()
    print currentMax[0]
    if currentMax[0] == None:
        newid = 1
    else:
       newid = int(currentMax[0]) + 1
    command = "INSERT INTO blog(name, blog_id) VALUES('" + name + "'," + str(newid) +  ")"
    c.execute(command)
    conn.commit()
    conn.close()
    
def blog_list():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    blogs = []
    for row in c.execute("select name from blog"):
        blogs.append(row[0])
    print blogs
    return blogs

blog_list()

