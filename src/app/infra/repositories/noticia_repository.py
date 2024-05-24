from core.entities.noticia import Noticia
from infra.database import mysql


class NoticiaRepository:
    def create_noticia_record(self, noticia_record: Noticia):
        print(mysql, flush=True)

        sql = """
        INSERT INTO noticias
        (title, content, img)
        VALUES (%s, %s, %s)
        """
        params = [
            noticia_record.title,
            noticia_record.content,
            noticia_record.img,
        ]

        mysql.mutate(sql=sql, params=params)

    def get_noticias(self) -> list[Noticia]:
        select_query = "SELECT * FROM noticias"
        rows = mysql.query(sql=select_query, is_single=False)

        noticias = []

        for row in rows:
            noticias.append(self.__get_noticia_entity(row))

        return noticias
    
    def get_noticia_by_id(self, id: str) -> Noticia | None:
        row = mysql.query(
            sql="SELECT * FROM noticias WHERE id = %s",
            params=[id]
        )
        
        if row:
            return self.__get_noticia_entity(row)
        
        return None
    
    def get_latest_records(self, id: str) -> Noticia | None:
        select_query = "SELECT * FROM noticias ORDER BY created_at DESC LIMIT 3;"
        rows = mysql.query(sql=select_query, is_single=False)

        noticias = []

        for row in rows:
            noticias.append(self.__get_noticia_entity(row))

        return noticias

    def __get_noticia_entity(self, row):
        return Noticia(id=row["id"], title=row["title"], content=row["content"], img=row["img"], created_at=row["created_at"])
