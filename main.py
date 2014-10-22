## from /pythonfile/ import /function/
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import sqlite3
import populate
import os.path

app = Flask(__name__)

<<<<<<< HEAD

@app.route('/')
def index():
    if not os.path.isfile("blog.db"):
        populate.create_db()

    populate.add_blog("test blog")
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    blogs = c.execute("SELECT name FROM blogs")
    return render_template("home.html", blogs=blogs)
=======
conn = sqlite3.connect("blog.db")
c = conn.cursor()
c.execute("INSERT INTO blogs VALUES('Test Blog')")
conn.commit()

@app.route('/')
def index():
    
    return render_template("home.html")
>>>>>>> 6e571cc1396380d5bca654c2fc060367cf737be9
#Index page; will list name of all BLOGS (rather than posts)
#and have a form where one can create a new blog.
#Names should be unique, and be linked to a blog index.

@app.route('/<blogid>') 
def blogindex(blogid):
    pass
#Blog index; will list titles of all posts from blog and a form where
#one can enter new title and post.
#Titles should be unique, and should redirect user to a blog post page.

@app.route('/<blogid>/posts/<postid>')
def posts(blogid, postid):
    pass
#Blog post page; will show the title and content of a post in addition to
#comments. There should be ANOTHER form to add a new comment, and
#a way to get back to the main page.

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.debug=True
    app.run(port=5025)
