from flask_wtf import FlaskForm

from wtforms import StringField, ColorField
from wtforms.validators import DataRequired

from core.entities import Noticia


class NoticiaForm(FlaskForm):
    def __init__(self, formdata=None, noticia=None, **kwargs):
        super().__init__(formdata, **kwargs)

        if isinstance(noticia, Noticia):
            self.title.data = noticia.title
            self.content.data = noticia.cotent
            self.img.default = noticia.img

    title = StringField(
        "Titulo",
        validators=[DataRequired()],
    )

    content = StringField(
        "Conteudo",
        validators=[DataRequired()],
    )

    img = StringField(
        "Imagem",
        validators=[DataRequired()],
    )