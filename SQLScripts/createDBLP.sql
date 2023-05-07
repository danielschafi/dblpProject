
DROP TABLE IF EXISTS author;
CREATE TABLE author (
    ID serial PRIMARY KEY,
    orcId VARCHAR(255),
    name VARCHAR(255)
);

DROP TABLE IF EXISTS cite;
CREATE TABLE cite (
    ID serial PRIMARY KEY,
    ref VARCHAR(255)
);

DROP TABLE IF EXISTS editor;
CREATE TABLE editor (
    ID serial PRIMARY KEY,
    orcId VARCHAR(255),
    name VARCHAR (255)
);

DROP TABLE IF EXISTS ee;
CREATE TABLE ee (
    ID serial PRIMARY KEY,
    link VARCHAR(255)
);

DROP TABLE IF EXISTS eeType;
CREATE TABLE eeType (
    ID serial PRIMARY KEY,
    type VARCHAR(255)
);

DROP TABLE IF EXISTS journal;
CREATE TABLE journal (
    ID serial PRIMARY KEY,
    name VARCHAR(255)
);



DROP TABLE IF EXISTS school;
CREATE TABLE school (
    ID serial PRIMARY KEY,
    name VARCHAR(255)  
);

DROP TABLE IF EXISTS publisher;
CREATE TABLE publisher (
    ID serial PRIMARY KEY,
    name VARCHAR(255)
);





DROP TABLE IF EXISTS proceedings;
CREATE TABLE proceedings (
    ID serial PRIMARY KEY,
    title VARCHAR(255),
    year VARCHAR(25),
    url VARCHAR(255),
    publisherId int,
    isbn VARCHAR(255),
    key VARCHAR(255),
    CONSTRAINT fkPublisher
    FOREIGN KEY(publisherId)
    REFERENCES publisher(ID)
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
    title VARCHAR(255),
    year VARCHAR(255),
    crossref VARCHAR(255),
    booktitle VARCHAR(255),
    url VARCHAR(255),
    pages VARCHAR(255),
    key VARCHAR(255)
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
    crossref VARCHAR(255),
    title VARCHAR(255),
    note VARCHAR(255),
    number VARCHAR(255),
    month VARCHAR(25),
    year VARCHAR(25),
    key VARCHAR(255)
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
    title VARCHAR(255),
    note VARCHAR(255),
    -- authorListId int,
    year VARCHAR(25),
    key VARCHAR(255),
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
    series VARCHAR(255),
    title VARCHAR(255),
    isbn VARCHAR(255),
    note VARCHAR(255),
    number VARCHAR(255),
    pages VARCHAR(25),
    volume int,
    year VARCHAR(25),
    month VARCHAR(25),
    key VARCHAR(255)
    publisherId int,
    schoolId int,
    CONSTRAINT fkPublisher
    FOREIGN KEY(publisherId)
    REFERENCES publisher(ID),
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
    crossref VARCHAR(255),
    title VARCHAR(255),
    pages VARCHAR(25),
    booktitle VARCHAR(255),
    url VARCHAR(255),
    year VARCHAR(25),
    key VARCHAR(255)
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
    crossref VARCHAR(255),
    series VARCHAR(255),
    schoolId int,
    title VARCHAR(255),
    note VARCHAR(255),
    volume VARCHAR(255),
    pages VARCHAR(25),
    year VARCHAR(25),
    key VARCHAR(255),
    CONSTRAINT fkSchool
    FOREIGN KEY(schoolId)
    REFERENCES school(ID)
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
    crossref VARCHAR(255),
    title VARCHAR(255),
    note VARCHAR(255),
    url VARCHAR(255),
    key VARCHAR(255)
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
    number VARCHAR(255),
    pages VARCHAR(255),
    url VARCHAR(255),
    year VARCHAR(255),
    key VARCHAR(255),
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


