from flask import request, render_template

from core.use_cases import create_noticia_by_form
from core.commons import Error

from infra.forms import NoticiaForm


def create_noticia_view():
    if request.method == "POST":
        noticia_form = NoticiaForm(request.form)
        try:
            if not noticia_form.validate_on_submit():
                raise Error()

            create_noticia_by_form.execute(
                {
                    "title": noticia_form.title.data,
                    "content": noticia_form.content.data,
                    "img": noticia_form.img.data,
                }
            )
            return render_template("homepage.html")

        except Error as error:
            pass
    else:
        noticia_form = NoticiaForm()
    return render_template("cadastro.html", form=noticia_form)
