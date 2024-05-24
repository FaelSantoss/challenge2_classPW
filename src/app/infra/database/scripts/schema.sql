-- Active: 1716055461921@@127.0.0.1@3306@fael
CREATE DATABASE IF NOT EXISTS `bla`;

CREATE TABLE IF NOT EXISTS noticias (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title VARCHAR(255),
    content VARCHAR(255),
    img VARCHAR(255),
    data_criacao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
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