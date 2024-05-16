-- Active: 1715605010850@@127.0.0.1@3306@bla
CREATE DATABASE IF NOT EXISTS `bd`;

CREATE TABLE IF NOT EXISTS noticia (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title varchar(255),
    content varchar(255),
    img varchar(255)
);

SELECT * FROM noticia;