## from /pythonfile/ import /function/
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

conn = sqlite3.connect("blog.db")
c = conn.cursor()
c.execute("create table blogs(name text)")
c.execute("create table posts(title text, content text, author text, blog_id integer)")
c.execute("create table comments(content text, blog integer, author text)")
conn.commit()
c.execute("INSERT INTO blogs VALUES('Test Blog')")
conn.commit()

@app.route('/')
def index():
   
    blogs = c.execute("SELECT name FROM blogs")
    print blogs
    return render_template("home.html", blogs=blogs)
#Index page; will list name of all BLOGS (rather than posts)
#and have a form where one can create a new blog.
#Names should be unique, and be linked to a blog index.

@app.route('/<blogid>') 
def blogindex(blogid):
    pass
#Blog index; will list titles of all posts from blog and a form where
#one can enter new title and post.
#Titles should be unique, and should redirect user to a blog post page.

@app.route('/<postid>')
def posts(postid):
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
