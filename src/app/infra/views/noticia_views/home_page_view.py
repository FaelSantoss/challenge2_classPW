from flask import render_template

from infra.repositories import noticia_repository

def home_page_view():
    noticias = noticia_repository.get_noticias()
    latest_noticias = noticia_repository.get_latest_records()

    return render_template(
        "homepage.html",
        noticias=noticias,
        latest_noticias = latest_noticias
    )
