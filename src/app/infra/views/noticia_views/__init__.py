from flask import Blueprint, render_template

from .create_noticia_view import create_noticia_view
from .home_page_view import home_page_view
from .noticia_page_view import noticia_page_view

noticia_views = Blueprint("noticia_views", __name__)

@noticia_views.route("/")
def index():
    return home_page_view()

@noticia_views.route("/noticia/<id>")
def noticia(id):
    return noticia_page_view()

@noticia_views.route("/create-noticia", methods=["GET", "POST"])
def create_noticia():
    return create_noticia_view()
