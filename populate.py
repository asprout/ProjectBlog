import sqlite3

def create_db():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("create table blog (name text, blog_id integer)")
    c.execute("create table post(title text, content text, author text, blog_id integer, post_id integer)")
    c.execute("create table comment(content text, post_id integer, author text, comment_id integer)")
    conn.commit()
    conn.close()

def add_comment(author, content, postid):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    currentMax = c.execute("select max(comment_id) from comment").fetchone()
    if currentMax[0] == None:
        newid = 1
    else:
       newid = int(currentMax[0]) + 1
       command = "INSERT INTO comment(content, post_id, author, comment_id) VALUES("
       command += content + "'," + str(postid) + "'," + author + "'," + str(newid) + ")"
       c.execute(command)
       conn.commit()
       conn.close()

def comm_list(postid):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    comments = []
    for row in c.execute("SELECT author, content FROM comment WHERE post_id==" + postid):
        comments.append([row[0],row[1]])
    return comments

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
def get_blog(blogid):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    command = "SELECT name FROM blog WHERE blog_id==" + blogid
    for blog in c.execute(command):
        return blog[0]
    
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

def get_post(postid, blogid):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    post_dict = {}
    command = """
    SELECT title, content, author
    FROM post
    WHERE blog_id==""" + str(blogid) + """ and post_id==""" + str(postid)
    for post in c.execute(command):
        post_dict['title'] = post[0]
        post_dict['author'] = post[2]
        post_dict['content'] = post[1]
    return post_dict
