## from /pythonfile/ import /function/
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import sqlite3
import populate
import os.path

app = Flask(__name__)
#Index page; will list name of all POSTS
#and have a form where one can create a new post.
@app.route('/')
def index():
    if not os.path.isfile("blog.db"):
        populate.create_db()

    blogs = populate.blog_list()
    return render_template("home.html", blogs=blogs)


@app.route('/<blogid>') 
def blogindex(blogid):
    postlist = populate.post_list(blogid)
    return render_template("blog.html", postlist=postlist)
    
#Blog index; will list titles of all posts from blog and a form where
#one can enter new title and post.
#Titles should be unique, and should redirect user to a blog post page.

##@app.route('/viewpost/<postid>')
##def posts(blogid, postid):
    
#Blog post page; will show the title and content of a post in addition to
#comments. There should be ANOTHER form to add a new comment, and
#a way to get back to the main page.

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.debug=True
    app.run()
