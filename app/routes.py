# Microblog application routesself.
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Elijah' }
    posts = [
        {
            'author': { 'username': 'John' },
            'body': 'This is a flask microblog.'
        },
        {
            'author': { 'username': 'Eli' },
            'body': 'This is definitely a flask microblog.'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)
