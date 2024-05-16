from flask import Flask, request, render_template

from core.use_cases import create_noticia_by_form
from core.commons import Error

from infra.forms import NoticiaForm

import os
from werkzeug.utils import secure_filename

def create_app():
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )

    app.config["SECRET_KEY"] = "1234"
    app.config["UPLOAD_FOLDER"] = "static/fotos_noticias"

    return app

app = create_app()

def create_noticia_view():
    if request.method == "POST":
        noticia_form = NoticiaForm(request.form)
        try:
            if not noticia_form.validate_on_submit():
                raise Error()

            arquivo = noticia_form.img.data
            nome_seguro = secure_filename(arquivo.filename)

            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], nome_seguro)
            arquivo.save(caminho)

            create_noticia_by_form.execute(
                {
                    "title": noticia_form.title.data,
                    "content": noticia_form.content.data,
                    "img": nome_seguro,
                }
            )
            return render_template("homepage.html")

        except Error as error:
            pass
    else:
        noticia_form = NoticiaForm()
    return render_template("cadastro.html", form=noticia_form)
