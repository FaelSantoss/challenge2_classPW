from os import getenv
from typing import Union, Dict, List

import mysql.connector

class MySQL:
    __connection = None
    __database = None

    def __init__(self) -> None:
        config = {
            "user": getenv("MYSQL_DATABASE_USER"),
            "password": getenv("MYSQL_DATABASE_PASSWORD"),
            "database": getenv("MYSQL_DATABASE_NAME"),
            "host": getenv("MYSQL_DATABASE_HOST"),
            "raise_on_warnings": True,
        }

        try:
            self.__connection = mysql.connector.connect(**config)
            self.__database = self.__connection.cursor(dictionary=True)
            print(self.__database)

        except mysql.connector.Error as error:
            print("error", error)
            pass

    def query(self, sql: str, params: List = None, is_single=True) -> Union[Dict, None]:
        try:
            self.__database.execute(sql, params=params if params is not None else [])

            if is_single:
                return self.__database.fetchone()

            return self.__database.fetchall()

        except mysql.connector.Error as error:
            self.__close_connection()

    def mutate(self, sql: str, params) -> Dict:
        try:
            self.__database.execute(sql, params)
            self.__connection.commit()

        except mysql.connector.Error as error:
            print("error", error)
            self.__connection.rollback()
            self.__close_connection()

    def __close_connection(self):
        self.__connection.close()
        self.__database.close()
