from core.entities.noticia import Noticia
from infra.database import mysql


class NoticiaRepository:
    def create_noticia_record(self, noticia_record: Noticia):
        sql = """
        INSERT INTO noticia
        (title, content, img)
        VALUES (%s, %s, %s)
        """
        params = [
            noticia_record.title,
            noticia_record.content,
            noticia_record.img,
        ]

        mysql.mutate(sql, params)