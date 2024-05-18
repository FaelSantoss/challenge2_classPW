from flask import render_template

from infra.repositories import noticia_repository
from infra.forms import NoticiaForm


def noticias_page_view():
    noticias = noticia_repository.get_noticias()

    return render_template(
        "homepage.html",
        noticias=noticias
    )
