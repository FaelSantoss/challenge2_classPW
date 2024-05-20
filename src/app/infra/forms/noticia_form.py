from flask_wtf import FlaskForm

from wtforms import StringField
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

    img = StringField(
        "Imagem",
        validators=[DataRequired()],
    )
