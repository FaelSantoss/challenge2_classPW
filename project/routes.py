from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
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

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_noticia():
    if request.method == 'POST':
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']
        imagem = request.files['imagem']
        return redirect(url_for('index'))
    return render_template('cadastro.html')