CREATE DATABASE IF NOT EXISTS `bd`;

USE DATABASE `bd`;

CREATE TABLE IF NOT EXISTS noticia (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title varchar(255),
    content varchar(255),
    foto_id CHAR(36),
    FOREIGN KEY (foto_id) REFERENCES foto(id)
);