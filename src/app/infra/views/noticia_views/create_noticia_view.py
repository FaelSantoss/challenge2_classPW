from flask import Flask, request, render_template, redirect

from core.use_cases import create_noticia_by_form
from core.commons import Error

from infra.forms import NoticiaForm
from werkzeug.utils import secure_filename
import os

def create_noticia_view():
    
    img_path = 'default.jpg'

    if request.method == "POST":
        noticia_form = NoticiaForm(request.form)
        try:
            file = request.files.get('img')

            caminho = os.path.abspath(os.path.dirname(__file__))
            caminho_static = caminho.replace('app/infra/views/noticia_views', 'ui/static/uploads')

            if file and file.filename!= '':
                filename = secure_filename(file.filename)
                filepath = os.path.join(caminho_static, filename)
                file.save(filepath)
                img_path = filename

            create_noticia_by_form.execute(
                {
                    "title": noticia_form.title.data,
                    "content": noticia_form.content.data,
                    "img": img_path,
                }
            )
            return redirect('/')

        except Error as error:
            pass
    else:
        noticia_form = NoticiaForm()
    return render_template("cadastro.html", form=noticia_form)
