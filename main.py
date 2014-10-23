## from /pythonfile/ import /function/
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import sqlite3
import populate
import os.path

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if not os.path.isfile("blog.db"):
        populate.create_db()
    blogs = populate.blog_list()
    if request.method=="GET":
        return render_template("home.html", blogs=blogs)
    else:
        if request.form['b']=="Create":
            blog_title=request.form["newblogtitle"]
            populate.add_blog(blog_title)
            blogs = populate.blog_list()
            return render_template("home.html", blogs=blogs)

@app.route('/<blogid>', methods=["GET","POST"]) 
def blogindex(blogid):
    blog_name = populate.get_blog(blogid)
    postlist = populate.post_list(blogid)
    if request.method=="GET":
        return render_template("blog.html", postlist=postlist, blogid=blogid, blog_name=blog_name)
    else:
        if request.form['b']=="Submit":
            post_title=request.form["newposttitle"]
            post_name=request.form["newpostname"]
            post_content=request.form["newpostcontent"]
            populate.add_post(post_title, post_content, post_name, blogid)
            postlist = populate.post_list(blogid)
            return render_template("blog.html", postlist=postlist, blogid=blogid, blog_name=blog_name)

#Blog index; will list titles of all posts from blog and a form where
#one can enter new title and post.
#Titles should be unique, and should redirect user to a blog post page.

@app.route('/<blogid>/viewpost/<postid>', methods=["GET","POST"])
def posts(postid, blogid):
    post_dict = populate.get_post(postid, blogid)
    comments = populate.comm_list(postid)
    if request.method=="GET":
        return render_template("post.html", post_dict=post_dict, comments=comments)
    else:
        if request.form['b']=="Submit":
            comment_author = request.form['author']
            comment_content = request.form['content']
            populate.add_comment(comment_author, comment_content, postid)
            comments = populate.comm_list(postid)
            return render_template("post.html", post_dict=post_dict, comments=comments)
    
#Blog post page; will show the title and content of a post in addition to
#comments. There should be ANOTHER form to add a new comment, and
#a way to get back to the main page.

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.debug=True
    app.run()
