-- Active: 1716055461921@@127.0.0.1@3306@fael
CREATE DATABASE IF NOT EXISTS `fael`;

CREATE TABLE IF NOT EXISTS noticias (
    id CHAR(36) DEFAULT(UUID()) PRIMARY KEY NOT NULL,
    title varchar(255),
    content varchar(255),
    img varchar(255)
);

SELECT * FROM noticias;

DROP TABLE noticias;
