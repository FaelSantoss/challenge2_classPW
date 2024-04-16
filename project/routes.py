from flask import render_template, url_for
from project import app

@app.route('/')
def index():
    return render_template("homepage.html")

@app.route('/noticia1')
def noticia1():
    return render_template("noticia1.html")

@app.route('/noticia2')
def noticia2():
    return render_template("noticia2.html")

@app.route('/noticia3')
def noticia3():
    return render_template("noticia3.html")