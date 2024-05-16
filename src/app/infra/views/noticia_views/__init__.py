from flask import Blueprint, render_template, request
from .create_noticia_view import create_noticia_view
import os
from werkzeug.utils import secure_filename

from ....app import create_app

app = create_app()

create_noticia_view = create_noticia_view

noticia_views = Blueprint("noticia_views", __name__)


@noticia_views.route("/")
def index():
    return render_template("homepage.html")


@noticia_views.route("/noticia1")
def noticia1():
    return render_template("noticia1.html")


@noticia_views.route("/noticia2")
def noticia2():
    return render_template("noticia2.html")


@noticia_views.route("/noticia3")
def noticia3():
    return render_template("noticia3.html")


@noticia_views.route("/create-noticia", methods=["GET", "POST"])
def create_noticia():
    return create_noticia_view()


@noticia_views.route("/upload", methods=["POST"])
def upload_file():
    if "img" not in request.files:
        return "Nenhuma imagem foi enviada!", 400
    file = request.files["img"]
    if file.filename == "":
        return "Nenhuma imagem foi selecionada.", 400
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return f"Arquivo {filename} enviado com sucesso!"
