from flask import render_template, url_for
from project import app

@app.route('/')
def index():
    return render_template("homepage.html")

@app.route('/teste')
def teste():
    return render_template("teste.html")