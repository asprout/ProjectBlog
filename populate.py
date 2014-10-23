import sqlite3

def create_db():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("create table blog (name text, blog_id integer)")
    c.execute("create table post(title text, content text, author text, blog_id integer, post_id integer)")
    c.execute("create table comment(content text, post_id integer, author text)")
    conn.commit()
    conn.close()
    
def add_blog(name):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    currentMax = c.execute("select max(blog_id) from blog").fetchone()
    if currentMax[0] == None:
        newid = 1
    else:
       newid = int(currentMax[0]) + 1
    command = "INSERT INTO blog(name, blog_id) VALUES('" + name + "'," + str(newid) +  ")"
    c.execute(command)
    conn.commit()
    conn.close()

def add_post(title, content, author, blog_id):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    currentMax = c.execute("select max(post_id) from post").fetchone()
    if currentMax[0] == None:
        newid = 1
    else:
       newid = int(currentMax[0]) + 1
    command = "INSERT INTO post(title, content, author, blog_id, post_id) VALUES('" + title + "','" + content + "','" + author + "','" + str(blog_id) + "','" + str(newid) +  "')"
    c.execute(command)
    conn.commit()
    conn.close()
    
def blog_list():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    blogs = []
    for row in c.execute("select name, blog_id from blog"):
        blogs.append([row[0],row[1]])
    return blogs

def post_list(blogid):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    posts = []
    for row in c.execute("select title,  author, post_id from post where blog_id==" + str(blogid)):
        posts.append([row[0],row[1],row[2]])
    return posts
