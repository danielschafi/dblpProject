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
        "title" : getattr(article.find("title"), "text", None),
        "number" : getattr(article.find("number"),"text", None),
        "pages" : getattr(article.find("pages"),"text", None),
        "url" : getattr(article.find("url"),"text", None),
        "year" : getattr(article.find("year"),"text", None),
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
                "eeid" : e,
                "pw" : pw
            }
            createArticleEeList(json.dumps(articleEeDict))

def parseInproceedings(inproceedings):
    authorIDList = parseAuthors(inproceedings.findall("author"))
    eeIDList = parseEes(inproceedings.findall("ee"))
    
    inproceedingsDict = {
        "title" : inproceedings.find("title").text,
        "year" : inproceedings.find("year").text,
        "crossref" : inproceedings.find("crossref").text,
        "booktitle" : inproceedings.find("booktitle").text,
        "url" : inproceedings.find("url").text,
        "pages" : inproceedings.find("pages").text,
        "pw" : pw
    }
    
    
    createInproceedings(json.dumps(inproceedingsDict))
    inproceedingsID = getInproceedingsID(inproceedingsDict["url"])

    if authorIDList:
        for a in authorIDList:
            inproceedingsAuthorDict = {
                "inproceedingsid" : inproceedingsID,
                "authorid" : a,
                "pw" : pw
            }
            createInproceedingsAuthorList(json.dumps(inproceedingsAuthorDict))

    if eeIDList:
        for e in eeIDList:
            inproceedingsEeDict = {
                "inproceedingsid" : inproceedingsID,
                "eeid" : e,
                "pw" : pw
            }
            createInproceedingsEeList(json.dumps(inproceedingsEeDict))

def parseProceedings(proceedings):
    publisherID = parsePublisher(proceedings.find("publisher"))
    eeIDList = parseEes(proceedings.findall("ee"))
    editorIDList = parseEditors(proceedings.findall("editor"))
    
    # Haben (zumindest in den testdaten) noch mehr properties und ees
    proceedingsDict = {
        "title" : proceedings.find("title").text,
        "year" : proceedings.find("year").text,
        "url" : proceedings.find("url").text,
        "publisherId": publisherID,
        "isbn" : proceedings.find("isbn").text,
        "pw" : pw,
    }
    
    createProceedings(json.dumps(proceedingsDict))
    proceedingsID = getProceedingsID(proceedingsDict["url"])

    if eeIDList:
        for e in eeIDList:
            proceedingsEeDict = {
                "proceedingsid" : proceedingsID,
                "eeid" : e,
                "pw" : pw
            }
            createProceedingsEeList(json.dumps(proceedingsEeDict))

    if editorIDList:
        for e in editorIDList:
            proceedingsEditorDict = {
                "proceedingsid" : proceedingsID,
                "editorid" : e,
                "pw" : pw
            }
            createProceedingsEditorList(json.dumps(proceedingsEditorDict))

def parseBook(book):
    schoolID = parseSchool(book.find("school"))
    authorIDList = parseAuthors(book.findall("author"))
    eeIDList = parseEes(book.findall("ee"))
    editorIDList = parseEditors(book.findall("editor"))
    
    bookDict = {
        "crossref" : book.find("crossref").text,
        "series" : book.find("series").text,
        "schoolId" : schoolID,
        "title" : book.find("title").text,
        "note" : book.find("note").text,
        "volume" : book.find("volume").text,
        "pages" : book.find("pages").text,
        "year" : book.find("year").text,
    }
    
    createBook(json.dumps(bookDict))
    bookID = getBookID(bookDict["url"])

    if eeIDList:
        for e in eeIDList:
            bookEeDict = {
                "bookid" : bookID,
                "eeid" : e,
                "pw" : pw
            }
            createBookEeList(json.dumps(bookEeDict))

    if editorIDList:
        for e in editorIDList:
            bookEditorDict = {
                "bookid" : bookID,
                "editorid" : e,
                "pw" : pw
            }
            createBookEditorList(json.dumps(bookEditorDict))
    
    if authorIDList:
        for a in authorIDList:
            bookAuthorDict = {
                "bookid" : bookID,
                "authorid" : a,
                "pw" : pw
            }
            createBookAuthorList(json.dumps(bookAuthorDict))
                
def parseincollection(incollection):
    authorIDList = parseAuthors(incollection.findall("author"))
    eeIDList = parseEes(incollection.findall("ee"))
    citeIDList = parseCites(incollection.findall("cite"))

    incollectionDict = {
        "crossref" : incollection.find("crossref").text,
        "title" : incollection.find("title").text,
        "pages" : incollection.find("pages").text,
        "booktitle" : incollection.find("booktitle").text,
        "url" : incollection.find("url").text,
        "year" : incollection.find("year").text,
    }
    
    createIncollection(json.dumps(incollectionDict))
    incollectionID = getIncollectionID(incollectionDict["url"])

    if authorIDList:
        for a in authorIDList:
            incollectionAuthorDict = {
                "incollectionid" : incollectionID,
                "authorid" : a,
                "pw" : pw
            }
            createIncollectionAuthorList(json.dumps(incollectionAuthorDict))

    if eeIDList:
        for e in eeIDList:
            incollectionEeDict = {
                "incollectionid" : incollectionID,
                "eeid" : e,
                "pw" : pw
            }
            createIncollectionEeList(json.dumps(incollectionEeDict))

    if citeIDList:
        for c in citeIDList:
            incollectionCiteDict = {
                "incollectionid" : incollectionID,
                "citeid" : c,
                "pw" : pw
            }
            createIncollectionCiteList(json.dumps(incollectionCiteDict))

def parsephdthesis(phdthesis):
    schoolID = parseSchool(phdthesis.find("school"))
    publisherID = parsePublisher(phdthesis.find("publisher"))
    authorIDList = parseAuthors(phdthesis.findall("author"))
    eeIDList = parseEes(phdthesis.findall("ee"))

    phdthesisDict = {
        "series" : phdthesis.find("series").text,
        "title" : phdthesis.find("title").text,
        "isbn" : phdthesis.find("isbn").text,
        "note" : phdthesis.find("note").text,
        "number" : phdthesis.find("number").text,
        "pages" : phdthesis.find("pages").text,
        "volume" : phdthesis.find("volume").text,
        "year" : phdthesis.find("year").text,
        "month" : phdthesis.find("month").text,
        "schoolId" : schoolID,
        "publisherId": publisherID,
    }
    
    createPhdthesis(json.dumps(phdthesisDict))
    phdthesisID = getPhdthesisID(phdthesisDict["url"])

    if authorIDList:
        for a in authorIDList:
            phdthesisAuthorDict = {
                "phdthesisid" : phdthesisID,
                "authorid" : a,
                "pw" : pw
            }
            createPhdthesisAuthorList(json.dumps(phdthesisAuthorDict))

    if eeIDList:
        for e in eeIDList:
            phdthesisEeDict = {
                "phdthesisid" : phdthesisID,
                "eeid" : e,
                "pw" : pw
            }
            createPhdthesisEeList(json.dumps(phdthesisEeDict))

def parseMastersthesis(mastersthesis):
    schoolID = parseSchool(mastersthesis.find("school"))
    authorIDList = parseAuthors(mastersthesis.findall("author"))
    eeIDList = parseEes(mastersthesis.findall("ee"))

    mastersthesisDict = {
        "title" : mastersthesis.find("title").text,
        "note" : mastersthesis.find("note").text,
        "year" : mastersthesis.find("year").text,
        "schoolId" : schoolID,
    }
    
    createMastersthesis(json.dumps(mastersthesisDict))
    mastersthesisID = getMastersthesisID(mastersthesisDict["url"])

    if authorIDList:
        for a in authorIDList:
            mastersthesisAuthorDict = {
                "mastersthesisid" : mastersthesisID,
                "authorid" : a,
                "pw" : pw
            }
            createMastersthesisAuthorList(json.dumps(mastersthesisAuthorDict))

    if eeIDList:
        for e in eeIDList:
            mastersthesisEeDict = {
                "mastersthesisid" : mastersthesisID,
                "eeid" : e,
                "pw" : pw
            }
            createMastersthesisEeList(json.dumps(mastersthesisEeDict))

def parseWww(www):
    citeIDList = parseCites(www.findall("cite"))

    wwwDict = {
        "crossref" : www.find("crossref").text,
        "title" : www.find("title").text,
        "note" : www.find("note").text,
        "url" : www.find("url").text,
    }
    
    createWWW(json.dumps(wwwDict))
    wwwID = getWWWID(wwwDict["url"])

    if citeIDList:
        for c in citeIDList:
            wwwCiteDict = {
                "wwwid" : wwwID,
                "citeid" : c,
                "pw" : pw
            }
            createWWWCiteList(json.dumps(wwwCiteDict))

def parseData(data):
    authorIDList = parseAuthors(data.findall("author"))
    eeIDList = parseEes(data.findall("ee"))
    dataDict = {
        "crossref" : data.find("crossref").text,
        "title" : data.find("title").text,
        "note" : data.find("note").text,
        "number" : data.find("number").text,
        "month" : data.find("month").text,
        "year" : data.find("year").text,
    }
    createData(json.dumps(dataDict))
    dateID = getDataID(dataDict["url"])

    if authorIDList:
        for a in authorIDList:
            dataAuthorDict = {
                "dataid" : dateID,
                "authorid" : a,
                "pw" : pw
            }
            createDataAuthorList(json.dumps(dataAuthorDict))

    if eeIDList:
        for e in eeIDList:
            dataEeDict = {
                "dataid" : dateID,
                "eeid" : e,
                "pw" : pw
            }
            createDataEeList(json.dumps(dataEeDict))


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

def parsePublisher(publisher):
    publisherID = getPublisherID(publisher.text)
    if publisherID is None:
        publisherDict = {
            "name" : publisher.text,
            "pw" : 1234
        }
        createPublisher(json.dumps(publisherDict))
        publisherID = getPublisherID(publisher.text)   
    return publisherID

def parseAuthors(authors):
    authorIDList = []
    for a in authors:
        authorID = getAuthorID(getattr(a.get("orcid"), "text", None), a.text)
        if authorID is None:
            authorDict = {
                "orcid": getattr(a.get("orcid"), "text", None),
                "name": a.text,
                "pw": pw
            }
            createAuthor(json.dumps(authorDict))
            authorIDList.append(getAuthorID(getattr(a.get("orcid"), "text", None), a.text))
        else:
            authorIDList.append(authorID)
    return authorIDList or None

def parseSchool(school):
    schoolID = getSchoolID(school.text)
    if schoolID is None:
        schoolDict = {
            "name" : school.text,
            "pw" : 1234
        }
        createSchool(json.dumps(schoolDict))
        schoolID = getSchoolID(school.text)   
    return schoolID

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

def parseCites(cites):
    citeIDList = []
    for c in cites:
        citeID = getCiteID(c.text)
        if citeID is None:
            citeDict = {
                "ref": c.text,
                "pw": pw
            }
            createCite(json.dumps(citeDict))
            citeIDList.append(getCiteID(c.text))
        else:
            citeIDList.append(citeID)
    return citeIDList or None

def parseEeType(eeType):
    eeTypeID = getEeTypeID(eeType.text)
    if eeTypeID is None:
        eeTypeDict = {
            "type" : eeType.text,
            "pw" : 1234
        }
        createEeType(json.dumps(eeTypeDict))
        eeTypeID = getEeTypeID(eeType.text)   
    return eeTypeID

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
            createEditor(json.dumps(editorDict))
            editorIDList.append(getEditorID(e.get("orcid"), e.text))
        else:
            editorIDList.append(editorID)
    return editorIDList or None
            
    # if eeIDList:
    #     for e in eeIDList:
    #         proceedingsEeDict = {
    #             "proceedingsid" : proceedingsID,
    #             "eeid" : e,
    #             "pw" : pw
    #         }
    #         createProceedingsEeList(json.dumps(proceedingsEeDict))