## from /pythonfile/ import /function/
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    pass
#Index page; will list name of all BLOGS (rather than posts) and have a form where one can create a new blog. Names should be unique, and be linked to a blog index.

@app.route('/BLOGIDHERE') 
def blogindex():
    pass
#Blog index; will list titles of all posts from blog and a form where one can enter new title and post. Titles should be unique, and should redirect user to a blog post page.

@app.route('/POSTIDHERE')
def posts():
    pass
#Blog post page; will show the title and content of a post in addition to comments. There should be ANOTHER form to add a new comment, and a way to get back to the main page.

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.debug=True
    app.run(port=5025)
