from flask import render_template

from infra.repositories import noticia_repository

def noticia_page_view():
    noticias = noticia_repository.get_noticias()

    return render_template(
        "noticia1.html",
        noticias=noticias
    )
