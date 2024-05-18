from flask import Flask, request, render_template, redirect

from core.use_cases import create_noticia_by_form
from core.commons import Error

from infra.forms import NoticiaForm

import os
from werkzeug.utils import secure_filename

def create_noticia_view():
    if request.method == "POST":
        noticia_form = NoticiaForm(request.form)
        try:
            if not noticia_form.validate_on_submit():
                raise Error()

            #uploaded_file = noticia_form.img.data
            #filename = secure_filename(uploaded_file.filename)
            #file_path = os.path.join("static/fotos_noticias", filename)
            #uploaded_file.save(file_path)
            img = 'fotos_noticias/default.jpg'
            create_noticia_by_form.execute(
                {
                    "title": noticia_form.title.data,
                    "content": noticia_form.content.data,
                    "img": img,
                }
            )
            return redirect('/')

        except Error as error:
            pass
    else:
        noticia_form = NoticiaForm()
    return render_template("cadastro.html", form=noticia_form)
