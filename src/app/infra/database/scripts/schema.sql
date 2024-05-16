-- Active: 1715889620255@@127.0.0.1@3306
CREATE DATABASE IF NOT EXISTS `bd`;

CREATE TABLE IF NOT EXISTS noticia (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title varchar(255),
    content varchar(255),
    img varchar(255)
);

SELECT * FROM noticia;