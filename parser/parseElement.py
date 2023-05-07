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
    articleID = getArticleID(article.get("key"))
    if articleID is None:
        if article is None: return None
        journalID = parseJournal(article.find("journal"))
        authorIDList = parseAuthors(article.findall("author"))
        eeIDList = parseEes(article.findall("ee"))
        
        articleDict = {
            "title" : getattr(article.find("title"), "text",""),
            "number" : getattr(article.find("number"),"text",""),
            "pages" : getattr(article.find("pages"),"text",""),
            "url" : getattr(article.find("url"),"text",""),
            "year" : getattr(article.find("year"),"text",""),
            "volume" : getattr(article.find("volume"),"text",""),
            "key" : article.get("key"),
            "journalid" : journalID or 1,
            "pw" : pw
        }
        
        createArticle(json.dumps(articleDict))
        articleID = getArticleID(article.get("key"))

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
    inproceedingsID = getInproceedingsID(inproceedings.get("key"))
    if inproceedingsID is None:
        if inproceedings is None: return None
        authorIDList = parseAuthors(inproceedings.findall("author"))
        eeIDList = parseEes(inproceedings.findall("ee"))
        
        inproceedingsDict = {
            "title" : getattr(inproceedings.find("title"),"text",""),
            "year" : getattr(inproceedings.find("year") , "text",""),
            "crossref" : getattr(inproceedings.find("crossref"), "text",""),
            "booktitle" : getattr(inproceedings.find("booktitle"), "text",""),
            "url" : getattr(inproceedings.find("url"),"text",""),
            "pages" : getattr(inproceedings.find("pages"), "text",""),
            "key" : inproceedings.get("key"),
            "pw" : pw
        }
        
        #TODO Adjust queries in get to search for key instead
        createInproceedings(json.dumps(inproceedingsDict))
        inproceedingsID = getInproceedingsID(inproceedings.get("key"))
        
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
    proceedingsID = getProceedingsID(proceedings.get("key"))
    if proceedingsID is None:
        if proceedings is None: return None
        publisherID = parsePublisher(proceedings.find("publisher"))
        eeIDList = parseEes(proceedings.findall("ee"))
        editorIDList = parseEditors(proceedings.findall("editor"))
        seriesID = parseSeries(proceedings.find("series"))

        
        # Haben (zumindest in den testdaten) noch mehr properties und ees
        proceedingsDict = {
            "title" : getattr(proceedings.find("title"), "text",""),
            "booktitle" : getattr(proceedings.find("booktitle"), "text",""),
            "seriesid" : seriesID or 1,
            "volume" : getattr(proceedings.find("volume"),"text",""),
            "year" : getattr(proceedings.find("year"),"text",""),
            "url" : getattr(proceedings.find("url"),"text",""),
            "isbn" : getattr(proceedings.find("isbn"), "text",""),
            "key" : proceedings.get("key"),
            "publisherid": publisherID or 1,
            "pw" : pw,
        }
        
        createProceedings(json.dumps(proceedingsDict))
        proceedingsID = getProceedingsID(proceedings.get("key"))

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
    bookID = getBookID(book.get("key"))
    if bookID is None:
        if book is None: return None
        schoolID = parseSchool(book.find("school"))
        publisherID = parsePublisher(book.find("publisher"))
        seriedID = parseSeries(book.find("series"))
        authorIDList = parseAuthors(book.findall("author"))
        eeIDList = parseEes(book.findall("ee"))
        editorIDList = parseEditors(book.findall("editor"))
        
        bookDict = {
            "crossref" : getattr(book.find("crossref"), "text",""),
            "seriesid" : seriedID or 1,
            "schoolid" : schoolID or 1,
            "publisherid" : publisherID or 1,
            "title" : getattr(book.find("title"), "text",""),
            "note" : getattr(book.find("note"), "text",""),
            "volume" : getattr(book.find("volume"), "text",""),
            "pages" : getattr(book.find("pages"), "text",""),
            "year" : getattr(book.find("year"), "text",""),
            "isbn" : getattr(book.find("isbn"), "text",""),
            "key" : book.get("key"),
            "pw" : pw,
        }
        
        createBook(json.dumps(bookDict))
        bookID = getBookID(book.get("key"))

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
                
def parseIncollection(incollection):
    incollectionID = getIncollectionID(incollection.get("key"))
    if incollectionID is None:
        if incollection is None: return None
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
            "key" : incollection.get("key"),
            "pw" : pw
        }
        
        createIncollection(json.dumps(incollectionDict))
        incollectionID = getIncollectionID(incollection.get("key"))

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

def parsePhdthesis(phdthesis):
    phdthesisID = getPhdthesisID(phdthesis.get("key"))
    if phdthesisID is None:
        if phdthesis is None: return None
        schoolID = parseSchool(phdthesis.find("school"))
        publisherID = parsePublisher(phdthesis.find("publisher"))
        seriesID = parseSeries(phdthesis.find("series"))
        authorIDList = parseAuthors(phdthesis.findall("author"))
        eeIDList = parseEes(phdthesis.findall("ee"))

        phdthesisDict = {
            "series" : seriesID or 1,
            "title" : getattr(phdthesis.find("title"),"text",""),
            "isbn" : getattr(phdthesis.find("isbn"),"text",""),
            "note" : getattr(phdthesis.find("note"),"text",""),
            "number" : getattr(phdthesis.find("number"),"text",""),
            "pages" : getattr(phdthesis.find("pages"),"text",""),
            "volume" : getattr(phdthesis.find("volume"),"text",""),
            "year" : getattr(phdthesis.find("year"),"text",""),
            "month" : getattr(phdthesis.find("month"),"text",""),
            "key" : phdthesis.get("key"),
            "schoolid" : schoolID or 1,
            "publisherid": publisherID or 1,
            "pw" : pw
        }
        
        createPhdthesis(json.dumps(phdthesisDict))
        phdthesisID = getPhdthesisID(phdthesis.get("key"))

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
    mastersthesisID = getMastersthesisID(mastersthesis.get("key"))
    if mastersthesisID is None:
        if mastersthesis is None: return None
        schoolID = parseSchool(mastersthesis.find("school"))
        authorIDList = parseAuthors(mastersthesis.findall("author"))
        eeIDList = parseEes(mastersthesis.findall("ee"))

        mastersthesisDict = {
            "title" : getattr(mastersthesis.find("title"),"text",""),
            "note" : getattr(mastersthesis.find("note"),"text",""),
            "year" : getattr(mastersthesis.find("year"),"text",""),
            "key" : mastersthesis.get("key"),
            "schoolid" : schoolID or 1,
            "pw" : pw
        }
        
        createMastersthesis(json.dumps(mastersthesisDict))
        mastersthesisID = getMastersthesisID(mastersthesis.get("key"))

        if authorIDList and mastersthesisID:
            for a in authorIDList:
                mastersthesisAuthorDict = {
                    "masterthesisid" : mastersthesisID,
                    "authorid" : a,
                    "pw" : pw
                }
                createMastersthesisAuthorList(json.dumps(mastersthesisAuthorDict))

        if eeIDList and mastersthesisID:
            for e in eeIDList:
                mastersthesisEeDict = {
                    "masterthesisid" : mastersthesisID,
                    "eeid" : e,
                    "pw" : pw
                }
                createMastersthesisEeList(json.dumps(mastersthesisEeDict))

def parseWww(www):
    wwwID = getWwwID(www.get("key"))
    if wwwID is None:
        if www is None: return None
        citeIDList = parseCites(www.findall("cite"))
        authorIDList = parseAuthors(www.findall("author"))

        wwwDict = {
            "crossref" : getattr(www.find("crossref"),"text",""),
            "title" : getattr(www.find("title"),"text",""),
            "note" : getattr(www.find("note"),"text",""),
            "url" : getattr(www.find("url"),"text",""),
            "key" : www.get("key"),
            "pw" : pw
        }
        
        createWWW(json.dumps(wwwDict))
        wwwID = getWwwID(www.get("key"))

        if citeIDList and wwwID:
            for c in citeIDList:
                wwwCiteDict = {
                    "wwwid" : wwwID,
                    "citeid" : c,
                    "pw" : pw
                }
                createWwwCiteList(json.dumps(wwwCiteDict))
        
        if authorIDList and wwwID:
            for a in authorIDList:
                wwwAuthorDict = {
                    "wwwid" : wwwID,
                    "authorid" : a,
                    "pw" : pw
                }
                createWwwAuthorList(json.dumps(wwwAuthorDict))

def parseData(data):
    dataID = getDataID(data.get("key"))
    if dataID is None:
        if data is None: return None
        authorIDList = parseAuthors(data.findall("author"))
        eeIDList = parseEes(data.findall("ee"))
        dataDict = {
            "crossref" : getattr(data.find("crossref"),"text",""),
            "title" : getattr(data.find("title"),"text",""),
            "note" : getattr(data.find("note"),"text",""),
            "number" : getattr(data.find("number"),"text",""),
            "month" : getattr(data.find("month"),"text",""),
            "year" : getattr(data.find("year"),"text",""),
            "key" : data.get("key"),
            "pw" : pw
        }
        createData(json.dumps(dataDict))
        dateID = getDataID(data.get("key"))

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
    if journal is None: return None
    if getattr(journal, "text") is None:
        return None
    journalID = getJournalID(journal.text)
    if journalID is None:
        journalDict = {
            "name" : journal.text,
            "pw" : pw
        }
        createJournal(json.dumps(journalDict))
        journalID = getJournalID(journal.text)   
    return journalID

def parsePublisher(publisher):
    if publisher is None: return None
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
    if authors is None: return None
    authorIDList = []
    for a in authors:
        orcid = a.get("orcid") or None
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
    if school is None: return None
    if getattr(school, "text") is None:
        return None  
    schoolID = getSchoolID(school.text)
    if schoolID is None:
        schoolDict = {
            "name" : school.text,
            "pw" : pw
        }
        createSchool(json.dumps(schoolDict))
        schoolID = getSchoolID(school.text)   
    return schoolID

def parseSeries(series):
    if series is None: return None
    if getattr(series, "text") is None:
        return None
    seriesID = getSeriesID(series.text)
    if seriesID is None:
        seriesDict = {
            "name" : series.text,
            "pw" : pw
        }
        createSeries(json.dumps(seriesDict))
        seriesID = getSeriesID(series.text)   
    return seriesID

def parseEes(ees):
    if ees is None: return None
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
    if cites is None: return None
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

#TODO EEType is not from xml, is different depending on where the ee is added, bzt check if it is needed at all
# def parseEeType(eeType):
#     if eeType is None: return None
#     if getattr(eeType, "text") is None:
#         return None  
#     eeTypeID = getEeTypeID(eeType.text)
#     if eeTypeID is None:
#         eeTypeDict = {
#             "type" : eeType.text,
#             "pw" : pw
#         }
#         createEeType(json.dumps(eeTypeDict))
#         eeTypeID = getEeTypeID(eeType.text)   
#     return eeTypeID


def parseEditors(editors):
    if editors is None: return None
    editorIDList = []
    for e in editors:
        orcid = e.get("orcid") or None
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