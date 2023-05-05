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

def getAuthorID(orcid,author):
    if orcid is not None:
        conn = engine.connect()
        query = text("SELECT * FROM author WHERE orcid = :orcid")
        query = query.bindparams(orcid=orcid)
        result = conn.execute(query)
        conn.close()
        for row in result:
            if row[0] is None:
                conn = engine.connect()
                query = text("SELECT * FROM author WHERE name = :author")
                query = query.bindparams(author=author)
                result = conn.execute(query)
                conn.close()
                for row in result:
                    return row[0]
            else:
                return None
    else:
        conn = engine.connect()
        query = text("SELECT * FROM author WHERE name = :author")
        query = query.bindparams(author=author)
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
    query = text("SELECT * FROM article WHERE url = :url")
    query = query.bindparams(url=article)
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