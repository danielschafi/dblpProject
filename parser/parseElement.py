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


