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
        "title" : getattr(article.find("title"), "text",""),
        "number" : getattr(article.find("number"),"text",""),
        "pages" : getattr(article.find("pages"),"text",""),
        "url" : getattr(article.find("url"),"text",""),
        "year" : getattr(article.find("year"),"text",""),
        "journalid" : journalID or "",
        "pw" : pw
    }
    
    createArticle(json.dumps(articleDict))
    articleID = getArticleID(articleDict.get("url"))

    if authorIDList and articleID:
        for a in authorIDList:
            articleAuthorDict = {
                "articleid" : articleID,
                "authorid" : a,
                "pw" : pw
            }
            createArticleAuthorList(json.dumps(articleAuthorDict))
            
    if eeIDList and articleID:
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
        "title" : getattr(inproceedings.find("title"),"text",""),
        "year" : getattr(inproceedings.find("year") , "text",""),
        "crossref" : getattr(inproceedings.find("crossref"), "text",""),
        "booktitle" : getattr(inproceedings.find("booktitle"), "text",""),
        "url" : getattr(inproceedings.find("url"),"text",""),
        "pages" : getattr(inproceedings.find("pages"), "text",""),
        "pw" : pw
    }
    
    
    createInproceedings(json.dumps(inproceedingsDict))
    inproceedingsID = getInproceedingsID(inproceedingsDict.get("url"))

    if authorIDList and inproceedingsID:
        for a in authorIDList:
            inproceedingsAuthorDict = {
                "inproceedingsid" : inproceedingsID,
                "authorid" : a,
                "pw" : pw
            }
            createInproceedingsAuthorList(json.dumps(inproceedingsAuthorDict))

    if eeIDList and inproceedingsID:
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
        "title" : getattr(proceedings.find("title"), "text",""),
        "year" : getattr(proceedings.find("year"),"text",""),
        "url" : getattr(proceedings.find("url"),"text",""),
        "publisherId": publisherID or "",
        "isbn" : getattr(proceedings.find("isbn"), "text",""),
        "pw" : pw,
    }
    
    createProceedings(json.dumps(proceedingsDict))
    proceedingsID = getProceedingsID(proceedingsDict.get("url"))

    if eeIDList and proceedingsID:
        for e in eeIDList:
            proceedingsEeDict = {
                "proceedingsid" : proceedingsID,
                "eeid" : e,
                "pw" : pw
            }
            createProceedingsEeList(json.dumps(proceedingsEeDict))

    if editorIDList and proceedingsID:
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
        "crossref" : getattr(book.find("crossref"), "text",""),
        "series" : getattr(book.find("series"), "text",""),
        "schoolId" : schoolID or "",
        "title" : getattr(book.find("title"), "text",""),
        "note" : getattr(book.find("note"), "text",""),
        "volume" : getattr(book.find("volume"), "text",""),
        "pages" : getattr(book.find("pages"), "text",""),
        "year" : getattr(book.find("year"), "text",""),
        "pw" : pw,
    }
    
    createBook(json.dumps(bookDict))
    bookID = getBookID(bookDict.get("url"))

    if eeIDList and bookID:
        for e in eeIDList:
            bookEeDict = {
                "bookid" : bookID,
                "eeid" : e,
                "pw" : pw
            }
            createBookEeList(json.dumps(bookEeDict))

    if editorIDList and bookID:
        for e in editorIDList:
            bookEditorDict = {
                "bookid" : bookID,
                "editorid" : e,
                "pw" : pw
            }
            createBookEditorList(json.dumps(bookEditorDict))
    
    if authorIDList and bookID:
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
        "crossref" : getattr(incollection.find("crossref"), "text",""),
        "title" : getattr(incollection.find("title"), "text",""),
        "pages" : getattr(incollection.find("pages"), "text",""),
        "booktitle" : getattr(incollection.find("booktitle"), "text",""),
        "url" : getattr(incollection.find("url"), "text",""),
        "year" : getattr(incollection.find("year"), "text",""),
        "pw" : pw
    }
    
    createIncollection(json.dumps(incollectionDict))
    incollectionID = getIncollectionID(incollectionDict.get("url"))

    if authorIDList and incollectionID:
        for a in authorIDList:
            incollectionAuthorDict = {
                "incollectionid" : incollectionID,
                "authorid" : a,
                "pw" : pw
            }
            createIncollectionAuthorList(json.dumps(incollectionAuthorDict))

    if eeIDList and incollectionID:
        for e in eeIDList:
            incollectionEeDict = {
                "incollectionid" : incollectionID,
                "eeid" : e,
                "pw" : pw
            }
            createIncollectionEeList(json.dumps(incollectionEeDict))

    if citeIDList and incollectionID:
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
        "series" : getattr(phdthesis.find("series"),"text",""),
        "title" : getattr(phdthesis.find("title"),"text",""),
        "isbn" : getattr(phdthesis.find("isbn"),"text",""),
        "note" : getattr(phdthesis.find("note"),"text",""),
        "number" : getattr(phdthesis.find("number"),"text",""),
        "pages" : getattr(phdthesis.find("pages"),"text",""),
        "volume" : getattr(phdthesis.find("volume"),"text",""),
        "year" : getattr(phdthesis.find("year"),"text",""),
        "month" : getattr(phdthesis.find("month"),"text",""),
        "schoolId" : schoolID or "",
        "publisherId": publisherID or "",
        "pw" : pw
    }
    
    createPhdthesis(json.dumps(phdthesisDict))
    phdthesisID = getPhdthesisID(phdthesisDict.get("url"))

    if authorIDList and phdthesisID:
        for a in authorIDList:
            phdthesisAuthorDict = {
                "phdthesisid" : phdthesisID,
                "authorid" : a,
                "pw" : pw
            }
            createPhdthesisAuthorList(json.dumps(phdthesisAuthorDict))

    if eeIDList and phdthesisID:
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
        "title" : getattr(mastersthesis.find("title"),"text",""),
        "note" : getattr(mastersthesis.find("note"),"text",""),
        "year" : getattr(mastersthesis.find("year"),"text",""),
        "schoolId" : schoolID or "",
        "pw" : pw
    }
    
    createMastersthesis(json.dumps(mastersthesisDict))
    mastersthesisID = getMastersthesisID(mastersthesisDict["url"])

    if authorIDList and mastersthesisID:
        for a in authorIDList:
            mastersthesisAuthorDict = {
                "mastersthesisid" : mastersthesisID,
                "authorid" : a,
                "pw" : pw
            }
            createMastersthesisAuthorList(json.dumps(mastersthesisAuthorDict))

    if eeIDList and mastersthesisID:
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
        "crossref" : getattr(www.find("crossref"),"text",""),
        "title" : getattr(www.find("title"),"text",""),
        "note" : getattr(www.find("note"),"text",""),
        "url" : getattr(www.find("url"),"text",""),
        "pw" : pw
    }
    
    createWWW(json.dumps(wwwDict))
    wwwID = getWWWID(wwwDict.get("url"))

    if citeIDList and wwwID:
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
        "crossref" : getattr(data.find("crossref"),"text",""),
        "title" : getattr(data.find("title"),"text",""),
        "note" : getattr(data.find("note"),"text",""),
        "number" : getattr(data.find("number"),"text",""),
        "month" : getattr(data.find("month"),"text",""),
        "year" : getattr(data.find("year"),"text",""),
        "pw" : pw
    }
    createData(json.dumps(dataDict))
    dateID = getDataID(dataDict.get("url"))

    if authorIDList and dateID:
        for a in authorIDList:
            dataAuthorDict = {
                "dataid" : dateID,
                "authorid" : a,
                "pw" : pw
            }
            createDataAuthorList(json.dumps(dataAuthorDict))

    if eeIDList and dateID:
        for e in eeIDList:
            dataEeDict = {
                "dataid" : dateID,
                "eeid" : e,
                "pw" : pw
            }
            createDataEeList(json.dumps(dataEeDict))


def parseJournal(journal):
    if getattr(journal, "text") is None:
        return None
    journalID = getJournalID(journal, "text")
    if journalID is None:
        journalDict = {
            "name" : journal.text,
            "pw" : 1234
        }
        createJournal(json.dumps(journalDict))
        journalID = getJournalID(journal.text)   
    return journalID

def parsePublisher(publisher):
    if getattr(publisher, "text") is None:
        return None
    publisherID = getPublisherID(publisher.text)
    if publisherID is None:
        publisherDict = {
            "name" : publisher.text,
            "pw" : pw
        }
        createPublisher(json.dumps(publisherDict))
        publisherID = getPublisherID(publisher.text)   
    return publisherID

def parseAuthors(authors):
    authorIDList = []
    for a in authors:
        orcid = getattr(a.get("orcid"), "text")
        name = getattr(a , "text")
        if orcid or name:
            authorID = getAuthorID(orcid, name)
            if authorID is None:
                authorDict = {
                    "orcid": orcid or "",
                    "name": name or "",
                    "pw": pw
                }
                createAuthor(json.dumps(authorDict))
                authorIDList.append(getAuthorID(orcid, name))
            else:
                authorIDList.append(authorID)
    return authorIDList or None

def parseSchool(school):
    if getattr(school, "text") is None:
        return None  
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
        link = getattr(ee, "text")
        if link is not None:
            eeID = getEeID(link)
            if eeID is None:
                eeDict = {
                    "link": link,
                    "pw": pw
                }
                createEe(json.dumps(eeDict))
                eeIDList.append(getEeID(link))
            else:
                eeIDList.append(eeID)
    return eeIDList or None

def parseCites(cites):
    citeIDList = []
    for c in cites:
        ref = getattr(c, "text")
        if ref is not None:
            citeID = getCiteID(ref)
            if citeID is None:
                citeDict = {
                    "ref": ref,
                    "pw": pw
                }
                createCite(json.dumps(citeDict))
                citeIDList.append(getCiteID(ref))
            else:
                citeIDList.append(citeID)
    return citeIDList or None

#TODO EEType is not from xml, is different depending on where the ee is added
def parseEeType(eeType):
    if getattr(eeType, "text") is None:
        return None  
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
        orcid = getattr(e.get("orcid"), "text")
        name = getattr(e , "text")
        if orcid or name:
            editorID = getEditorID(orcid, name)
            if editorID is None:
                editorDict = {
                    "name": name or "",
                    "orcid": orcid or "",
                    "pw": pw
                }
                createEditor(json.dumps(editorDict))
                editorIDList.append(getEditorID(orcid, name))
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