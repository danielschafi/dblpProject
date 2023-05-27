"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.bookModel import BookModel
from Models.schoolModel import SchoolModel
from Models.publisherModel import PublisherModel
from Models.seriesModel import SeriesModel
from Models.phdthesisModel import PhdthesisModel
from Models.articleModel import ArticleModel
from Models.dataModel import DataModel
from Models.masterthesisModel import MasterthesisModel
from Models.schoolModel import SchoolModel
from Models.incollectionModel import IncollectionModel
from Models.inproceedingsModel import InproceedingsModel
from Models.proceedingsModel import ProceedingsModel
from Models.wwwModel import WwwModel
from pseudocode import create_response
import os

class KeywordRes(Resource):

    def get(self, keyword):
        authors = []
        publishers = []
        schools = []
        series = []
        journals = []
        ees = []
        cites = []
        editors = []

        #get phdThesis with keyword in title
        phdThesis = self.getPhdThesis(kword=keyword, 
                                 publishersList=publishers,
                                 schoolsList=schools,
                                 seriesList=series,
                                 eeList=ees,
                                 authorList=authors)
        #get articles with keyword in title
        articles = self.getArticles(kword=keyword,
                                    journalList=journals,
                                    eeList=ees,
                                    authorList=authors)
        #Get data with keyword in title
        datas = self.getData(kword=keyword,
                                eeList=ees,
                                authorList=authors)
        #get incollections with keyword in title or booktitle
        incollections = self.getIncollections(kword=keyword,
                                              authorList=authors,
                                              eeList=ees,
                                              citeList=cites)
        #get inprocceedings with keyword in title or booktitle
        inproceedings = self.getInproceedings(kword=keyword,
                                              authorList=authors,
                                              eeList=ees)
        #get masterthesis with keyword in title
        masterthesi = self.getMasterThesis(kword=keyword,
                                           schoolsList=schools,
                                              authorList=authors,
                                              eeList=ees)
        #get proceedings with keyword in title or booktitle
        proceedings = self.getProceedings(kword=keyword,
                                          publishersList=publishers,
                                          seriesList=series,
                                          editorList=editors,
                                          eeList = ees)
        #get www model with keyword in title
        #TODO: WWWS Title are all Home Page?
        wwws = []
        #wwws = self.getWWW(kword=keyword)
        
        #get books with keyword in title
        books = self.getBooks(kword=keyword,
                              schoolsList=schools,
                              seriesList=series,
                              publishersList=publishers,
                                authorList=authors,
                                eeList=ees,
                                editorList=editors)
        
        publishers = list(set(publishers))
        authors = list(set(authors))
        schools = list(set(schools))
        series = list(set(series))
        journals = list(set(journals))
        ees = list(set(ees))
        authors = list(set(authors))
        cites = list(set(cites))
        editors = list(set(editors))

        return create_response(
            {
                "numberOfNodes": (len(phdThesis) + len(publishers)
                               + len(schools) + len(series)
                               + len(journals) + len(articles)
                               + len(datas) + len(masterthesi)
                               + len(books) + len(incollections)
                               + len(inproceedings) + len(wwws)
                               + len(authors) + len(ees)
                               + len(cites) + len(editors)),
                "phdthesis": phdThesis,
                "publisher": publishers,
                "school": schools,
                "series": series,
                "journal": journals,
                "article": articles,
                "data": datas,
                "masterthesis": masterthesi,
                "book": books,
                "incollection": incollections,
                "proceedings": proceedings,
                "inproceedings": inproceedings,
                "www": wwws,
                "author": authors,
                "ee": ees,
                "cite": cites,
                "editor": editors
           }, 200
        )

    def getPhdThesis(self, kword, publishersList,schoolsList,seriesList, authorList, eeList):
        thesisiIds, publisherIds, schoolsIds, seriesIds, authors, ees = PhdthesisModel.getNodesKeyword(kword)
        publishersList.extend(publisherIds)
        schoolsList.extend(schoolsIds)
        seriesList.extend(seriesIds)
        authorList.extend(authors)
        eeList.extend(ees)
        return thesisiIds
    
    def getArticles(self, kword, journalList, authorList, eeList):
        articlesIds, journalIds, authors, ees = ArticleModel.getNodesKeyword(kword)
        journalList.extend(journalIds)
        authorList.extend(authors)
        eeList.extend(ees)
        return articlesIds

    def getData(self, kword, authorList, eeList):
        dataIds, authors, ees = DataModel.getNodesKeyword(kword)
        authorList.extend(authors)
        eeList.extend(ees)
        return dataIds
    
    def getIncollections(self, kword, authorList, eeList, citeList):
        incollectionIds, authors, ees, cites = IncollectionModel.getNodesKeyword(kword)
        authorList.extend(authors)
        eeList.extend(ees)
        citeList.extend(cites)
        return incollectionIds
    
    def getMasterThesis(self, kword, schoolsList, authorList, eeList):
        masterThesisIds, schoolsIds, authors, ees = MasterthesisModel.getNodesKeyword(kword)
        schoolsList.extend(schoolsIds)
        authorList.extend(authors)
        eeList.extend(ees)
        return masterThesisIds
    
    def getBooks(self, kword, schoolsList, seriesList, publishersList, authorList, eeList, editorList):
        booksIds, schoolsIds, seriesIds, publishersIds, authors, ees, editors = BookModel.getNodesKeyword(kword)
        schoolsList.extend(schoolsIds)
        seriesList.extend(seriesIds)
        publishersList.extend(publishersIds)
        authorList.extend(authors)
        eeList.extend(ees)
        editorList.extend(editors)
        return booksIds
    
    def getProceedings(self, kword, seriesList, publishersList, editorList, eeList):
        proceedingsIds, seriesIds, publishersIds, editors, ees = ProceedingsModel.getNodesKeyword(kword)
        seriesList.extend(seriesIds)
        publishersList.extend(publishersIds)
        editorList.extend(editors)
        eeList.extend(ees)
        return proceedingsIds
    
    def getInproceedings(self, kword, authorList, eeList):
        inproceedingsIds, authors, ees = InproceedingsModel.getNodesKeyword(kword)
        authorList.extend(authors)
        eeList.extend(ees)
        return inproceedingsIds
    
    def getWWW(self, kword):
        wwwIds = WwwModel.getNodesKeyword(kword)
        return wwwIds

    



def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("crossref",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument("title",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("note",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("volume",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pages",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("isbn",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("year",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("key",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("schoolid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("publisherid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("seriesid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser