from flask import render_template, request

from infra.repositories import noticia_repository

def noticia_page_view():
    url = str(request.path)
    id = url.replace('/noticia/', '')
    noticia = noticia_repository.get_noticia_by_id(id=id)
    return render_template(
        "noticia.html",
        noticia = noticia
    )
