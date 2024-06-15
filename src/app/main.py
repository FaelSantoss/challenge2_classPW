from flask import Flask,Blueprint, render_template

from infra.views.noticia_views import create_noticia_view
from infra.views.noticia_views import home_page_view
from infra.views.noticia_views import noticia_page_view

from infra.views import init_views

def create_app():
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )

    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
    app.config["SECRET_KEY"] = "1234"
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg'}
    init_views(app)


    print(f"MAX_CONTENT_LENGTH: {app.config['MAX_CONTENT_LENGTH']}", flush=True)
    
    return app

app = create_app()
