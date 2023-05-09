
DROP TABLE IF EXISTS author;
CREATE TABLE author (
    ID serial PRIMARY KEY,
    orcId TEXT,
    name TEXT
);

DROP TABLE IF EXISTS cite;
CREATE TABLE cite (
    ID serial PRIMARY KEY,
    ref TEXT
);

DROP TABLE IF EXISTS editor;
CREATE TABLE editor (
    ID serial PRIMARY KEY,
    orcId TEXT,
    name VARCHAR (255)
);

DROP TABLE IF EXISTS ee;
CREATE TABLE ee (
    ID serial PRIMARY KEY,
    link TEXT
);

DROP TABLE IF EXISTS eeType;
CREATE TABLE eeType (
    ID serial PRIMARY KEY,
    type TEXT
);

DROP TABLE IF EXISTS journal;
CREATE TABLE journal (
    ID serial PRIMARY KEY,
    name TEXT
);



DROP TABLE IF EXISTS school;
CREATE TABLE school (
    ID serial PRIMARY KEY,
    name TEXT  
);

DROP TABLE IF EXISTS publisher;
CREATE TABLE publisher (
    ID serial PRIMARY KEY,
    name TEXT
);

DROP TABLE IF EXISTS series;
CREATE TABLE series (
    ID serial PRIMARY KEY,
    name TEXT
);





DROP TABLE IF EXISTS proceedings;
CREATE TABLE proceedings (
    ID serial PRIMARY KEY,
    title TEXT,
    booktitle TEXT,
    year TEXT,
    url TEXT,
    publisherId int,
    seriesId int,
    isbn TEXT,
    volume TEXT,
    key TEXT,
    CONSTRAINT fkPublisher
    FOREIGN KEY(publisherId)
    REFERENCES publisher(ID),
    CONSTRAINT fkSeries
    FOREIGN KEY(seriesId)
    REFERENCES series(ID)
);

DROP TABLE IF EXISTS proceedingsEeList;
CREATE TABLE proceedingsEeList(
    ID serial PRIMARY KEY,
    proceedingsId int,
    eeId int,
    CONSTRAINT fkProceedings
    FOREIGN KEY(proceedingsId)
    REFERENCES proceedings(ID) ON UPDATE CASCADE,
    CONSTRAINT fkEe
    FOREIGN KEY(eeId)
    REFERENCES ee(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS proceedingsEditorList;
CREATE TABLE proceedingsEditorList(
    ID serial PRIMARY KEY,
    proceedingsId int,
    editorId int,
    CONSTRAINT fkProceedings
    FOREIGN KEY(proceedingsId)
    REFERENCES proceedings(ID) ON UPDATE CASCADE,
    CONSTRAINT fkEditor
    FOREIGN KEY(editorId)
    REFERENCES editor(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS inproceedings;
CREATE TABLE inproceedings (
    ID serial PRIMARY KEY,
    title TEXT,
    year TEXT,
    crossref TEXT,
    booktitle TEXT,
    url TEXT,
    pages TEXT,
    key TEXT
);

DROP TABLE IF EXISTS inproceedingsEeList;
CREATE TABLE inproceedingsEeList(
    ID serial PRIMARY KEY,
    inproceedingsId int,
    eeId int,
    CONSTRAINT fkInproceedings
    FOREIGN KEY(inproceedingsId)
    REFERENCES inproceedings(ID) ON UPDATE CASCADE,
    CONSTRAINT fkEe
    FOREIGN KEY(eeId)
    REFERENCES ee(ID) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS inproceedingsAuthorList;
CREATE TABLE inproceedingsAuthorList(
    ID serial PRIMARY KEY,
    inproceedingsId int,
    authorId int,
    CONSTRAINT fkInproceedings
    FOREIGN KEY(inproceedingsId)
    REFERENCES inproceedings(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fkAuthor
    FOREIGN KEY(authorId)
    REFERENCES author(ID) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS data;
CREATE TABLE data (
    ID serial PRIMARY KEY,
    crossref TEXT,
    title TEXT,
    note TEXT,
    number TEXT,
    month VARCHAR(25),
    year TEXT,
    key TEXT
);


DROP TABLE IF EXISTS dataEeList;
CREATE TABLE dataEeList(
    ID serial PRIMARY KEY,
    dataId int,
    eeId int,
    CONSTRAINT fkData
    FOREIGN KEY(dataId)
    REFERENCES data(ID) ON UPDATE CASCADE,
    CONSTRAINT fkEe
    FOREIGN KEY(eeId)
    REFERENCES ee(ID) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS dataAuthorList;
CREATE TABLE dataAuthorList(
    ID serial PRIMARY KEY,
    dataId int,
    authorId int,
    CONSTRAINT fkData
    FOREIGN KEY(dataId)
    REFERENCES data(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fkAuthor
    FOREIGN KEY(authorId)
    REFERENCES author(ID) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS masterthesis;
CREATE TABLE masterthesis (
    ID serial PRIMARY KEY,
    title TEXT,
    note TEXT,
    year TEXT,
    key TEXT,
    schoolId int,
    CONSTRAINT fkSchool
    FOREIGN KEY(schoolId)
    REFERENCES school(ID)
);


DROP TABLE IF EXISTS masterthesisEeList;
CREATE TABLE masterthesisEeList(
    ID serial PRIMARY KEY,
    masterthesisId int,
    eeId int,
    CONSTRAINT fkMasterthesis
    FOREIGN KEY(masterthesisId)
    REFERENCES masterthesis(ID) ON UPDATE CASCADE, 
    CONSTRAINT fkEe
    FOREIGN KEY(eeId)
    REFERENCES ee(ID) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS masterthesisAuthorList;
CREATE TABLE masterthesisAuthorList(
    ID serial PRIMARY KEY,
    masterthesisId int,
    authorId int,
    CONSTRAINT fkMasterthesis
    FOREIGN KEY(masterthesisId)
    REFERENCES masterthesis(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fkAuthor
    FOREIGN KEY(authorId)
    REFERENCES author(ID) ON UPDATE CASCADE ON DELETE CASCADE
);



DROP TABLE IF EXISTS phdthesis;
CREATE TABLE phdthesis (
    ID serial PRIMARY KEY,
    seriesId int,
    title TEXT,
    isbn TEXT,
    note TEXT,
    number TEXT,
    pages TEXT,
    volume TEXT,
    year TEXT,
    month VARCHAR(25),
    key TEXT,
    publisherId int,
    schoolId int,
    CONSTRAINT fkPublisher
    FOREIGN KEY(publisherId)
    REFERENCES publisher(ID),
    CONSTRAINT fkSeries
    FOREIGN KEY(seriesId)
    REFERENCES series(ID),
    CONSTRAINT fkSchool
    FOREIGN KEY(schoolId)
    REFERENCES school(ID)
);

DROP TABLE IF EXISTS phdthesisEeList;
CREATE TABLE phdthesisEeList(
    ID serial PRIMARY KEY,
    phdthesisId int,
    eeId int,
    CONSTRAINT fkPhdthesis
    FOREIGN KEY(phdthesisId)
    REFERENCES phdthesis(ID) ON UPDATE CASCADE,
    CONSTRAINT fkEe
    FOREIGN KEY(eeId)
    REFERENCES ee(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS phdthesisAuthorList;
CREATE TABLE phdthesisAuthorList(
    ID serial PRIMARY KEY,
    phdthesisId int,
    authorId int,
    CONSTRAINT fkPhdthesis
    FOREIGN KEY(phdthesisId)
    REFERENCES phdthesis(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fkAuthor
    FOREIGN KEY(authorId)
    REFERENCES author(ID) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS incollection;
CREATE TABLE incollection (
    ID serial PRIMARY KEY,
    crossref TEXT,
    title TEXT,
    pages TEXT,
    booktitle TEXT,
    url TEXT,
    year TEXT,
    key TEXT
);

DROP TABLE IF EXISTS incollectionEeList;
CREATE TABLE incollectionEeList(
    ID serial PRIMARY KEY,
    incollectionId int,
    eeId int,
    CONSTRAINT fkIncollection
    FOREIGN KEY(incollectionId)
    REFERENCES incollection(ID) ON UPDATE CASCADE, 
    CONSTRAINT fkEe
    FOREIGN KEY(eeId)
    REFERENCES ee(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS incollectionAuthorList;
CREATE TABLE incollectionAuthorList(
    ID serial PRIMARY KEY,
    incollectionId int,
    authorId int,
    CONSTRAINT fkIncollection
    FOREIGN KEY(incollectionId)
    REFERENCES incollection(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fkAuthor
    FOREIGN KEY(authorId)
    REFERENCES author(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS incollectionCiteList;
CREATE TABLE incollectionCiteList(
    ID serial PRIMARY KEY,
    incollectionId int,
    citeId int,
    CONSTRAINT fkIncollection
    FOREIGN KEY(incollectionId)
    REFERENCES incollection(ID) ON UPDATE CASCADE,
    CONSTRAINT fkCite
    FOREIGN KEY(citeId)
    REFERENCES cite(ID) ON UPDATE CASCADE
);


DROP TABLE IF EXISTS book;
CREATE TABLE book (
    ID serial PRIMARY KEY,
    crossref TEXT,
    seriesId int,
    schoolId int,
    publisherId int,
    title TEXT,
    note TEXT,
    volume TEXT,
    pages TEXT,
    year TEXT,
    isbn TEXT,
    key TEXT,
    CONSTRAINT fkSchool
    FOREIGN KEY(schoolId)
    REFERENCES school(ID),
    CONSTRAINT fkPublisher
    FOREIGN KEY(publisherId)
    REFERENCES publisher(ID),
    CONSTRAINT fkSeries
    FOREIGN KEY(seriesId)
    REFERENCES series(ID)
);


DROP TABLE IF EXISTS bookEeList;
CREATE TABLE bookEeList(
    ID serial PRIMARY KEY,
    bookId int,
    eeId int,
    CONSTRAINT fkBook
    FOREIGN KEY(bookId)
    REFERENCES book(ID) ON UPDATE CASCADE, 
    CONSTRAINT fkEe
    FOREIGN KEY(eeId)
    REFERENCES ee(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS bookAuthorList;
CREATE TABLE bookAuthorList(
    ID serial PRIMARY KEY,
    bookId int,
    authorId int,
    CONSTRAINT fkBook
    FOREIGN KEY(bookId)
    REFERENCES book(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fkAuthor
    FOREIGN KEY(authorId)
    REFERENCES author(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS bookEditorList;
CREATE TABLE bookEditorList(
    ID serial PRIMARY KEY,
    bookId int,
    editorId int,
    CONSTRAINT fkBook
    FOREIGN KEY(bookId)
    REFERENCES book(ID) ON UPDATE CASCADE,
    CONSTRAINT fkEditor
    FOREIGN KEY(editorId)
    REFERENCES editor(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS www;
CREATE TABLE www (
    ID serial PRIMARY KEY,
    crossref TEXT,
    title TEXT,
    note TEXT,
    url TEXT,
    key TEXT
);

DROP TABLE IF EXISTS wwwAuthorList;
CREATE TABLE wwwAuthorList(
    ID serial PRIMARY KEY,
    wwwId int,
    authorId int,
    CONSTRAINT fkWww
    FOREIGN KEY(wwwId)
    REFERENCES www(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fkAuthor
    FOREIGN KEY(authorId)
    REFERENCES author(ID) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS wwwCiteList;
CREATE TABLE wwwCiteList(
    ID serial PRIMARY KEY,
    wwwId int,
    citeId int,
    CONSTRAINT fkWww
    FOREIGN KEY(wwwId)
    REFERENCES www(ID) ON UPDATE CASCADE,
    CONSTRAINT fkCite
    FOREIGN KEY(citeId)
    REFERENCES cite(ID) ON UPDATE CASCADE
);

DROP TABLE IF EXISTS article;
CREATE TABLE article (
    ID serial PRIMARY KEY,
    journalId int,
    title VARCHAR (255),
    number TEXT,
    pages TEXT,
    url TEXT,
    year TEXT,
    volume VARCHAR(25),
    key TEXT,
    CONSTRAINT fkJournal
    FOREIGN KEY(journalId)
    REFERENCES journal(ID)
);

DROP TABLE IF EXISTS articleEeList;
CREATE TABLE articleEeList(
    ID serial PRIMARY KEY,
    articleId int,
    eeId int,
    CONSTRAINT fkArticle
    FOREIGN KEY(articleId)
    REFERENCES article(ID) ON UPDATE CASCADE, 
    CONSTRAINT fkEe
    FOREIGN KEY(eeId)
    REFERENCES ee(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS articleAuthorList;
CREATE TABLE articleAuthorList(
    ID serial PRIMARY KEY,
    articleId int,
    authorId int,
    CONSTRAINT fkArticle
    FOREIGN KEY(articleId)
    REFERENCES article(ID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fkAuthor
    FOREIGN KEY(authorId)
    REFERENCES author(ID) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO school (name) VALUES ('Not Available');
INSERT INTO publisher (name) VALUES ('Not Available');
INSERT INTO series (name) VALUES ('Not Available');
INSERT INTO journal (name) VALUES ('Not Available');

