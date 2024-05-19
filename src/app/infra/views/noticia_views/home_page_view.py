from flask import render_template

from infra.repositories import noticia_repository

def home_page_view():
    noticias = noticia_repository.get_noticias()

    return render_template(
        "homepage.html",
        noticias=noticias
    )
