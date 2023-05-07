import requests
from sqlalchemy import create_engine, text
import json

url = "http://127.0.0.1:5000/api"
headers = {'Content-type': 'application/json'}

# create a database engine
engine = create_engine('postgresql://postgres:1234@localhost/dblp')



#TODO: create get methods for all endpoints
def getJournalID(journal):
    conn = engine.connect()
    query = text("SELECT * FROM journal WHERE name = :journal")
    query = query.bindparams(journal=journal)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getPublisherID(publisher):
    conn = engine.connect()
    query = text("SELECT * FROM publisher WHERE name = :publisher")
    query = query.bindparams(publisher=publisher)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None


def getAuthorID(orcid,author):
    if orcid is not None:
        conn = engine.connect()
        query = text("SELECT * FROM author WHERE orcid = :orcid")
        query = query.bindparams(orcid=orcid)
        result = conn.execute(query)
        conn.close()
        for row in result:
            return row[0]
    else:
        conn = engine.connect()
        query = text("SELECT * FROM author WHERE name = :author")
        query = query.bindparams(author=author)
        result = conn.execute(query)
        conn.close()
        for row in result:
            return row[0]
    return None


def getEditorID(orcid,editor):
    if orcid is not None:
        conn = engine.connect()
        query = text("SELECT * FROM editor WHERE orcid = :orcid")
        query = query.bindparams(orcid=orcid)
        result = conn.execute(query)
        conn.close()
        for row in result:
            if row[0] is None:
                conn = engine.connect()
                query = text("SELECT * FROM editor WHERE name = :editor")
                query = query.bindparams(editor=editor)
                result = conn.execute(query)
                conn.close()
                for row in result:
                    return row[0]
            else:
                return None
    else:
        conn = engine.connect()
        query = text("SELECT * FROM editor WHERE name = :editor")
        query = query.bindparams(editor=editor)
        result = conn.execute(query)
        conn.close()
        for row in result:
            return row[0]
    return None


def getInproceedingsID(inproceedings):
    conn = engine.connect()
    query = text("SELECT * FROM inproceedings WHERE key = :key")
    query = query.bindparams(key=inproceedings)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getProceedingsID(proceedings):
    conn = engine.connect()
    query = text("SELECT * FROM proceedings WHERE key = :key")
    query = query.bindparams(key=proceedings)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getBookID(book):
    conn = engine.connect()
    query = text("SELECT * FROM book WHERE key = :key")
    query = query.bindparams(key=book)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getIncollectionID(incollection):
    conn = engine.connect()
    query = text("SELECT * FROM incollection WHERE key = :key")
    query = query.bindparams(key=incollection)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getPhdthesisID(phdthesis):
    conn = engine.connect()
    query = text("SELECT * FROM phdthesis WHERE key = :key")
    query = query.bindparams(key=phdthesis)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getMastersthesisID(mastersthesis):
    conn = engine.connect()
    query = text("SELECT * FROM mastersthesis WHERE key = :key")
    query = query.bindparams(key=mastersthesis)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getWwwID(www):
    conn = engine.connect()
    query = text("SELECT * FROM www WHERE key = :key")
    query = query.bindparams(key=www)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getDataID(data):
    conn = engine.connect()
    query = text("SELECT * FROM data WHERE key = :key")
    query = query.bindparams(key=data)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getEeID(ee):
    conn = engine.connect()
    query = text("SELECT * FROM ee WHERE link = :ee")
    query = query.bindparams(ee=ee)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getArticleID(article):
    conn = engine.connect()
    query = text("SELECT * FROM article WHERE key = :key")
    query = query.bindparams(key=article)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getSchoolID(school):
    conn = engine.connect()
    query = text("SELECT * FROM school WHERE name = :school")
    query = query.bindparams(school=school)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def getCiteID(cite):
    conn = engine.connect()
    query = text("SELECT * FROM cite WHERE ref = :ref")
    query = query.bindparams(ref=cite)
    result = conn.execute(query)
    conn.close()
    for row in result:
        return row[0]
    return None

def createJournal(journal):
    response = requests.post(url=url+"/journal/1", data=journal, headers=headers)
    return response.status_code


def createPublisher(publisher):
    response = requests.post(url=url+"/publisher/1", data=publisher, headers=headers)
    return response.status_code

def createAuthor(author):
    response = requests.post(url=url + "/author/1", data=author, headers=headers)
    return response.status_code

def createCite(cite):
    response = requests.post(url=url+"/cite/1", data=cite, headers=headers)
    return response.status_code

def createEe(ee):
    response = requests.post(url=url+"/ee/1", data=ee, headers=headers)
    return response.status_code

def createSchool(school):
    response = requests.post(url=url+"/school/1", data=school, headers=headers)
    return response.status_code

def createEditor(editor):
    response = requests.post(url=url+"/editor/1", data=editor, headers=headers)
    return response.status_code


def createArticle(article):
    response = requests.post(url=url+"/article/1", data=article, headers=headers)
    return response.status_code

def createArticleAuthorList(articleAuthor):
    response = requests.post(url=url+"/articleauthorlist/1", data=articleAuthor, headers=headers)
    return response.status_code

def createArticleEeList(articleEe):
    response = requests.post(url=url+"/articleeelist/1", data=articleEe, headers=headers)
    return response.status_code


def createInproceedings(inproceedings):
    response = requests.post(url=url+"/inproceedings/1", data=inproceedings, headers=headers)
    return response.status_code

def createInproceedingsAuthorList(inproceedingsAuthor):
    response = requests.post(url=url+"/inproceedingsauthorlist/1", data=inproceedingsAuthor, headers=headers)
    return response.status_code

def createInproceedingsEeList(inproceedingsEe):
    response = requests.post(url=url+"/inproceedingseelist/1", data=inproceedingsEe, headers=headers)
    return response.status_code


def createProceedings(proceedings):
    response = requests.post(url=url+"/proceedings/1", data=proceedings, headers=headers)
    return response.status_code

def createProceedingsEditorList(proceedingsEditor):
    response = requests.post(url=url+"/proceedingseditorlist/1", data=proceedingsEditor, headers=headers)
    return response.status_code

def createProceedingsEeList(proceedingsEe):
    response = requests.post(url=url+"/proceedingseelist/1", data=proceedingsEe, headers=headers)
    return response.status_code


def createBook(book):
    response = requests.post(url=url+"/book/1", data=book, headers=headers)
    return response.status_code

def createBookAuthorList(bookAuthor):
    response = requests.post(url=url+"/bookauthorlist/1", data=bookAuthor, headers=headers)
    return response.status_code

def createBookEeList(bookEe):
    response = requests.post(url=url+"/bookeelist/1", data=bookEe, headers=headers)
    return response.status_code

def createBookEditorList(bookEditor):
    response = requests.post(url=url+"/bookeditorlist/1", data=bookEditor, headers=headers)
    return response.status_code


def createIncollection(incollection):
    response = requests.post(url=url+"/incollection/1", data=incollection, headers=headers)
    return response.status_code

def createIncollectionAuthorList(incollectionAuthor):
    response = requests.post(url=url+"/incollectionauthorlist/1", data=incollectionAuthor, headers=headers)
    return response.status_code

def createIncollectionEeList(incollectionEe):
    response = requests.post(url=url+"/incollectioneelist/1", data=incollectionEe, headers=headers)
    return response.status_code

def createIncollectionCiteList(incollectionCite):
    response = requests.post(url=url+"/incollectioncitelist/1", data=incollectionCite, headers=headers)
    return response.status_code


def createPhdthesis(phdthesis):
    response = requests.post(url=url+"/phdthesis/1", data=phdthesis, headers=headers)
    return response.status_code

def createPhdthesisAuthorList(phdthesisAuthor):
    response = requests.post(url=url+"/phdthesisauthorlist/1", data=phdthesisAuthor, headers=headers)
    return response.status_code

def createPhdthesisEeList(phdthesisEe):
    response = requests.post(url=url+"/phdthesiseelist/1", data=phdthesisEe, headers=headers)
    return response.status_code


def createMastersthesis(mastersthesis):
    response = requests.post(url=url+"/masterthesis/1", data=mastersthesis, headers=headers)
    return response.status_code

def createMastersthesisAuthorList(mastersthesisAuthor):
    response = requests.post(url=url+"/masterthesisauthorlist/1", data=mastersthesisAuthor, headers=headers)
    return response.status_code

def createMastersthesisEeList(mastersthesisEe):
    response = requests.post(url=url+"/masterthesiseelist/1", data=mastersthesisEe, headers=headers)
    return response.status_code


def createWWW(www):
    response = requests.post(url=url+"/www/1", data=www, headers=headers)
    return response.status_code

def createWwwCiteList(wwwCite):
    response = requests.post(url=url+"/wwwcitelist/1", data=wwwCite, headers=headers)
    return response.status_code


def createData(data):
    response = requests.post(url=url+"/data/1", data=data, headers=headers)
    return response.status_code

def createDataAuthorList(dataAuthor):
    response = requests.post(url=url+"/dataauthorlist/1", data=dataAuthor, headers=headers)
    return response.status_code

def createDataEeList(dataEe):
    response = requests.post(url=url+"/dataeelist/1", data=dataEe, headers=headers)
    return response.status_code
