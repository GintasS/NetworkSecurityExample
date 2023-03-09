"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from NetworkSec import app
from cookiecutter.main import cookiecutter

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/', methods=['POST'])
def form_post():
    if request.method == 'POST':
        form_data = request.form['number1']
        # checkout = "--config=alias.checkout=!touch /mnt/c/Users/Domantas/VulnerableService/HELLO"
        cookiecutter('hg+https://hg.reactionary.software/repo/cookiecutter-vulnerable/', checkout=form_data)
        return request.form['number1']
    else:
        return render_template('index.html')
