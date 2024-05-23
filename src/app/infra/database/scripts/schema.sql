-- Active: 1715605010850@@127.0.0.1@3306@bla
CREATE DATABASE IF NOT EXISTS `bla`;

CREATE TABLE IF NOT EXISTS noticias (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title varchar(255),
    content varchar(255),
    img varchar(255)
);

SELECT * FROM noticias;

INSERT INTO
    noticias (title, content, img)
VALUES (
        'Título da Notícia',
        'Conteúdo da notícia',
        'URL_da_imagem'
    );

DROP TABLE noticias;