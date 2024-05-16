from flask import Blueprint, render_template
from .create_noticia_view import create_noticia_view

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
