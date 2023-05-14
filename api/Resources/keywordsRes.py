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
        #get phdThesis with keyword in title
        phdThesis = self.getPhdThesis(kword=keyword, 
                                 publishersList=publishers,
                                 schoolsList=schools,
                                 seriesList=series)
        #get articles with keyword in title
        articles = self.getArticles(kword=keyword,
                                    journalList=journals)
        #Get data with keyword in title
        datas = self.getData(kword=keyword)
        #get incollections with keyword in title or booktitle
        incollections = self.getIncollections(kword=keyword)
        #get inprocceedings with keyword in title or booktitle
        inproceedings = self.getInproceedings(kword=keyword)
        #get masterthesis with keyword in title
        masterthesi = self.getMasterThesis(kword=keyword,
                                           schoolsList=schools)
        #get proceedings with keyword in title or booktitle
        proceedings = self.getProceedings(kword=keyword,
                                          publishersList=publishers,
                                          seriesList=series)
        #get www model with keyword in title
        #TODO: WWWS Title are all Home Page?
        wwws = []
        #wwws = self.getWWW(kword=keyword)
        
        #get books with keyword in title
        books = self.getBooks(kword=keyword,
                              schoolsList=schools,
                              seriesList=series,
                              publishersList=publishers)
        publishers = list(set(publishers))
        authors = list(set(authors))
        schools = list(set(schools))
        series = list(set(series))
        journals = list(set(journals))

        return create_response(
            {
                "numberOfNodes": (len(phdThesis) + len(publishers)
                               + len(schools) + len(series)
                               + len(journals) + len(articles)
                               + len(datas) + len(masterthesi)
                               + len(books) + len(incollections)
                               + len(inproceedings) + len(wwws)),
                "phdthesis": phdThesis,
                "publishers": publishers,
                "schools": schools,
                "series": series,
                "journals": journals,
                "articles": articles,
                "datas": datas,
                "masterthesi": masterthesi,
                "books": books,
                "incollections": incollections,
                "proceedings": proceedings,
                "inproceedings": inproceedings,
                "www": wwws
           }, 200
        )

    def getPhdThesis(self, kword, publishersList,schoolsList,seriesList):
        thesisiIds, publisherIds, schoolsIds, seriesIds = PhdthesisModel.getNodesKeyword(kword)
        publishersList.extend(publisherIds)
        schoolsList.extend(schoolsIds)
        seriesList.extend(seriesIds)
        return thesisiIds
    
    def getArticles(self, kword, journalList):
        articlesIds, journalIds = ArticleModel.getNodesKeyword(kword)
        journalList.extend(journalIds)
        return articlesIds

    def getData(self, kword):
        dataIds = DataModel.getNodesKeyword(kword)
        return dataIds
    
    def getIncollections(self, kword):
        incollectionIds = IncollectionModel.getNodesKeyword(kword)
        return incollectionIds
    
    def getMasterThesis(self, kword, schoolsList):
        masterThesisIds, schoolsIds = MasterthesisModel.getNodesKeyword(kword)
        schoolsList.extend(schoolsIds)
        return masterThesisIds
    
    def getBooks(self, kword, schoolsList, seriesList, publishersList):
        booksIds, schoolsIds, seriesIds, publishersIds = BookModel.getNodesKeyword(kword)
        schoolsList.extend(schoolsIds)
        seriesList.extend(seriesIds)
        publishersList.extend(publishersIds)
        return booksIds
    
    def getProceedings(self, kword, seriesList, publishersList):
        proceedingsIds, seriesIds, publishersIds = ProceedingsModel.getNodesKeyword(kword)
        seriesList.extend(seriesIds)
        publishersList.extend(publishersIds)
        return proceedingsIds
    
    def getInproceedings(self, kword):
        inproceedingsIds = InproceedingsModel.getNodesKeyword(kword)
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