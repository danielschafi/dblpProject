import json 
import requests
import lxml.etree as etree
from getDBRelation import *



"""
parseXXXX methods 
param: element from xml with type XXXX
return: dict of the element
-> Add dict to list 
"""
pw = 1234

def parseArticle(article):
    journalID = parseJournal(article.find("journal"))
    authorIDList = parseAuthors(article.findall("author"))
    eeIDList = parseEes(article.findall("ee"))
    
    articleDict = {
        "title" : article.find("title").text,
        "number" : article.find("number").text,
        "pages" : article.find("pages").text,
        "url" : article.find("url").text,
        "year" : article.find("year").text,
        "journalid" : journalID,
        "pw" : pw
    }
    
    createArticle(json.dumps(articleDict))
    articleID = getArticleID(articleDict["url"])

    if authorIDList:
        for a in authorIDList:
            articleAuthorDict = {
                "articleid" : articleID,
                "authorid" : a,
                "pw" : pw
            }
            createArticleAuthorList(json.dumps(articleAuthorDict))
            
    if eeIDList:
        for e in eeIDList:
            articleEeDict = {
                "articleid" : articleID,
                "eeId" : e,
                "pw" : pw
            }
            createArticleEeList(json.dumps(articleEeDict))


def parseJournal(journal):
    journalID = getJournalID(journal.text)
    if journalID is None:
        journalDict = {
            "name" : journal.text,
            "pw" : 1234
        }
        createJournal(json.dumps(journalDict))
        journalID = getJournalID(journal.text)   
    return journalID

def parseAuthors(authors):
    authorIDList = []
    for a in authors:
        authorID = getAuthorID(a.get("orcid").text, a.text)
        if authorID is None:
            authorDict = {
                "orcid": a.get("orcid").text,
                "name": a.text,
                "pw": pw
            }
            createAuthor(json.dumps(authorDict))
            authorIDList.append(getAuthorID(a.get("orcid"), a.text))
        else:
            authorIDList.append(authorID)
    return authorIDList or None

def parsePublisher(publisher):
    publisherID = getPublisherID(publisher.text)
    if publisherID is None:
        publisherDict = {
            "name" : publisher.text,
            "pw" : 1234
        }
        createJournal(json.dumps(publisherDict))
        publisherID = getPublisherID(publisher.text)   
    return publisherID

def parseCites(cites):
    citeIDList = []
    for c in cites:
        citeID = getCiteID(c.text)
        if citeID is None:
            citeDict = {
                "ref": c.text,
                "pw": pw
            }
            createAuthor(json.dumps(citeDict))
            citeIDList.append(getCiteID(c.text))
        else:
            citeIDList.append(citeID)
    return citeIDList or None

def parseEes(ees):
    eeIDList = []
    for ee in ees:
        eeID = getEeID(ee.text)
        if eeID is None:
            eeDict = {
                "link": ee.text,
                "pw": pw
            }
            createEe(json.dumps(eeDict))
            eeIDList.append(getEeID(ee.text))
        else:
            eeIDList.append(eeID)
    return eeIDList or None


def parseEeType(eeType):
    eeTypeID = getPublisherID(eeType.text)
    if eeTypeID is None:
        eeTypeDict = {
            "type" : eeType.text,
            "pw" : 1234
        }
        createJournal(json.dumps(eeTypeDict))
        eeTypeID = getPublisherID(eeType.text)   
    return eeTypeID

def parseSchool(school):
    schoolID = getSchoolID(school.text)
    if schoolID is None:
        schoolDict = {
            "name" : school.text,
            "pw" : 1234
        }
        createJournal(json.dumps(schoolDict))
        schoolID = getPublisherID(school.text)   
    return schoolID

def parseEditors(editors):
    editorIDList = []
    for e in editors:
        editorID = getEditorID(e.get("orcid"), e.text)
        if editorID is None:
            editorDict = {
                "name": e.text,
                "orcid": e.get("orcid"),
                "pw": pw
            }
            createAuthor(json.dumps(editorDict))
            editorIDList.append(getEditorID(e.get("orcid"), e.text))
        else:
            editorIDList.append(editorID)
    return editorIDList or None