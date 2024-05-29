from core.commons import Error
from werkzeug.utils import secure_filename
from PIL import Image
import os


class UploadImgByForm:
    def execute(self, file):
        caminho = os.path.abspath(os.path.dirname(__file__))
        caminho_static = caminho.replace("app/core/use_cases", "ui/static/uploads")

        try:
            if file and file.filename != "":
                file.thumbnail((941, 627))
                filename = secure_filename(file.filename)
                filepath = os.path.join(caminho_static, filename)
                file.save(filepath)

        except Error as error:
            raise error
