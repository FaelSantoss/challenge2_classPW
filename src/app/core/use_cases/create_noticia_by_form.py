from core.entities.noticia import Noticia
from core.commons import Error
from infra.repositories import noticia_repository


class CreateNoticiaByForm:
    def execute(self, request: dict) -> None:
        try:
            noticia = Noticia(title=request["title"], content=request["content"], img=request["img"])

            noticia_repository.create_noticia_record(noticia)

        except Error as error:
            raise error