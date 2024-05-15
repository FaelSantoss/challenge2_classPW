from flask import request, render_template, redirect, url_for
from infra import app
from infra.views import create_noticia_view

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

@app.route('/create-noticia', methods=['GET', 'POST'])
def create_noticia():
    return create_noticia_view()
