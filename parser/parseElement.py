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

def parseArticle(element):
    journalID = parseJournal(element.find("journal"))
    authors = parseAuthors(element.findall("author").text)
    #  ee = parseEe
    
    articleDict = {
        "title" : element.find("title").text,
        "number" : element.find("number").text,
        "pages" : element.find("pages").text,
        "url" : element.find("url").text,
        "year" : element.find("year").text,
        "journalid" : journalID,
    }
    createArticle(json.dumps(articleDict)) # probably password missing
    
    if authors:
        #todo create articleAuthorList here
        pass
    


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
            createAuthor(json.dumps(a))
            authorIDList.append(getAuthorID(a))
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

def parseEe(ees):
    eeIDList = []
    for e in ees:
        eeID = getEeID(e)
        if eeID is None:
            createEe(json.dumps(e))
            eeIDList.append(getEeID(e))
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
