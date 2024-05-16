from flask import Flask
from .noticia_views import noticia_views


def init_views(app: Flask):
    app.register_blueprint(noticia_views)
