from core.commons import Error
from werkzeug.utils import secure_filename
from PIL import Image
import os
from io import BytesIO

class UploadImgByForm:
    def execute(self, file):
        caminho = os.path.abspath(os.path.dirname(__file__))
        caminho_static = caminho.replace("app/core/use_cases", "ui/static/uploads")

        try:
            if file and file.filename!= "":
                # Convertendo o arquivo para uma imagem usando BytesIO
                img_data = BytesIO(file.read())
                img = Image.open(img_data)
                
                # Criando uma miniatura
                img.thumbnail((941, 627), Image.Resampling.LANCZOS)
                
                # Salvando a imagem na pasta static/uploads
                filename = secure_filename(file.filename)
                filepath = os.path.join(caminho_static, filename)
                img.save(filepath)
                
                # Limpar o buffer de memória após uso
                img_data.close()

        except Error as error:
            raise error

