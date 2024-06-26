from flask_wtf import FlaskForm

from wtforms import StringField, FileField
from wtforms.validators import DataRequired


class NoticiaForm(FlaskForm):
    title = StringField(
        "Titulo",
        validators=[DataRequired()],
    )

    content = StringField(
        "Conteudo",
        validators=[DataRequired()],
    )

    img = FileField(
        "Imagem",
        validators=[DataRequired()],
    )
