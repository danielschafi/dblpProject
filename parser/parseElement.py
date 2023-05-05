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
    authorIDList = parseAuthors(article.findall("author").text)
    eeIDList = parseEes(article.findall("ee").text)
    
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
    articleID = getArticleID(article)

    if authorIDList:
        for a in authorIDList:
            articleAuthorDict = {
                "articleid" : articleID,
                "authorid" : a,
                "pw" : pw
            }
            createArticleAuthorList(json.dumps(articleAuthorDict))
            
    if eeIDList:
        for a in eeIDList:
            articleEeDict = {
                "articleid" : articleID,
                "eeId" : a,
                "pw" : pw
            }
            createArticleEeList(json.dumps(articleEeDict))


def parseJournal(element):
    journalID = getJournalID(element)
    if journalID is None:
        createJournal(json.dumps(element))
        journalID = getJournalID(element)   
    return journalID

def parseAuthors(authors):
    authorIDList = []
    for a in authors:
        authorID = getAuthorID(a)
        if authorID is None:
            authorDict = {
                "orcid": a.get("orcid"),
                "name": a.text,
                "pw": pw
            }
            createAuthor(json.dumps(authorDict))
            authorIDList.append(getAuthorID(a))
        else:
            authorIDList.append(authorID)
    return authorIDList or None

def parsePublisher(publishers):
    publisherIDList = []
    for p in publishers:
        publisherID = getPublisherID(p)
        if publisherID is None:
            createPublisher(json.dumps(p))
            publisherIDList.append(getPublisherID(p))
    return publisherIDList or None

def parseCites(cites):
    citesIDList = []
    for c in cites:
        citesID = getCiteID(c)
        if citesID is None:
            createCite(json.dumps(c))
            citesIDList.append(getCiteID(c))
    return citesIDList or None

def parseEes(ees):
    eeIDList = []
    for ee in ees:
        eeID = getEeID()(ee)
        if eeID is None:
            eeDict = {
                "link": ee.text,
                "pw": pw
            }
            createEe(json.dumps(eeDict))
            eeIDList.append(getEeID(ee))
        else:
            eeIDList.append(eeID)
    return eeIDList or None




def parseEeType(eeTypes):
    eeTypeIDList = []
    for e in eeTypes:
        eeTypeID = getEeTypeID(e)
        if eeTypeID is None:
            createEeType(json.dumps(e))
            eeTypeIDList.append(getEeTypeID(e))
    return eeTypeIDList or None

def parseSchool(schools):
    schoolIDList = []
    for s in schools:
        schoolID = getSchoolID(s)
        if schoolID is None:
            createSchool(json.dumps(s))
            schoolIDList.append(getSchoolID(s))
    return schoolIDList or None

def parseEditor(editors):
    editorIDList = []
    for e in editors:
        editorID = getEditorID(e)
        if editorID is None:
            createEditor(json.dumps(e))
            editorIDList.append(getEditorID(e))
    return editorIDList or None
