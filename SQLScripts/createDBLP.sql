CREATE DATABASE dblp

CREATE TABLE IF NOT EXISTS proceedings (
    ID serial PRIMARY KEY,
    ee int,
    editor VARCHAR(255),
    title VARCHAR(255),
    year VARCHAR(25),
    url VARCHAR(255),
    publisherId int,
    isbn VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS inproceedings (
    ID serial PRIMARY KEY,
    authorId int,
    title VARCHAR(255),
    year VARCHAR(255),
    crossref VARCHAR(255),
    booktitle VARCHAR(255),
    eeListId int,
    url int,
    pages VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS data (
    ID serial PRIMARY KEY,
    crossref VARCHAR(255),
    ee int,
    title VARCHAR(255),
    note VARCHAR(255),
    authorlistId int,
    number VARCHAR(255),
    month VARCHAR(25),
    year VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS masterthesis (
    ID serial PRIMARY KEY,
    ee int,
    title VARCHAR(255),
    note VARCHAR(255),
    authorlistId int,
    year VARCHAR(25),
    school int
);

CREATE TABLE IF NOT EXISTS phdthesis (
    ID serial PRIMARY KEY,
    series VARCHAR(255),
    ee int,
    title VARCHAR(255),
    isbn VARCHAR(255),
    note VARCHAR(255),
    authorlistId int,
    number VARCHAR(255),
    pages VARCHAR(25),
    volume int,
    year VARCHAR(25),
    month VARCHAR(25),
    publisherId int,
    school int
);

CREATE TABLE IF NOT EXISTS incollection (
    ID serial PRIMARY KEY,
    crossref VARCHAR(255),
    ee int,
    title VARCHAR(255),
    authorlistId int,
    pages VARCHAR(25),
    booktitle VARCHAR(255),
    cite int,
    url VARCHAR(255),
    year VARCHAR(25)    
);

CREATE TABLE IF NOT EXISTS book (
    ID serial PRIMARY KEY,
    crossref VARCHAR(255),
    series VARCHAR(255),
    ee int,
    school int,
    editor int,
    title VARCHAR(255),
    note VARCHAR(255),
    authorlistId int,
    volume VARCHAR(255),
    pages VARCHAR(25),
    year VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS www (
    ID serial PRIMARY KEY,
    crossref VARCHAR(255),
    title VARCHAR(255),
    note VARCHAR(255),
    cite int,
    url VARCHAR(255)    
);


CREATE TABLE IF NOT EXISTS article (
    ID serial PRIMARY KEY,
    journalId int,
    eeListId int,
    title VARCHAR (255),
    authorlistId int,
    number VARCHAR(255),
    pages VARCHAR(255),
    url VARCHAR(255),
    year VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS author (
    ID serial PRIMARY KEY,
    orcId VARCHAR(255),
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS cite (
    ID serial PRIMARY KEY,
    ref VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS editor (
    ID serial PRIMARY KEY,
    orcId VARCHAR(255),
    name VARCHAR (255)
);

CREATE TABLE IF NOT EXISTS ee (
    ID serial PRIMARY KEY,
    link VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS journal (
    ID serial PRIMARY KEY,
    name VARCHAR(255)
);





CREATE TABLE IF NOT EXISTS authorlist (
    ID serial PRIMARY KEY,
    listNr int,
    authorId int
);

CREATE TABLE IF NOT EXISTS citelist (
    ID serial PRIMARY KEY,
    listNr int,
    citeId int
);


CREATE TABLE IF NOT EXISTS editorlist (
    ID serial PRIMARY KEY,
    listNr int,
    editorId int
);


CREATE TABLE IF NOT EXISTS eelist (
    ID serial PRIMARY KEY,
    listNr int,
    eeId int
);


CREATE TABLE IF NOT EXISTS school (
    ID serial PRIMARY KEY,
    name VARCHAR(255)  
);

CREATE TABLE IF NOT EXISTS publisher (
    ID serial PRIMARY KEY,
    name VARCHAR(255)
);