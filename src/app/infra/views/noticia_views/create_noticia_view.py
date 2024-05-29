from flask import request, render_template, redirect

from core.use_cases import create_noticia_by_form, upload_img_by_form
from core.commons import Error

from infra.forms import NoticiaForm


def create_noticia_view():
    img_path = "default.jpg"

    if request.method == "POST":
        noticia_form = NoticiaForm(request.form)
        try:
            file = request.files.get("img")
            img_path = file.filename

            upload_img_by_form.execute(file=file)

            create_noticia_by_form.execute(
                {
                    "title": noticia_form.title.data,
                    "content": noticia_form.content.data,
                    "img": img_path,
                }
            )
            return redirect("/")

        except Error as error:
            pass
    else:
        noticia_form = NoticiaForm()
    return render_template("cadastro.html", form=noticia_form)
