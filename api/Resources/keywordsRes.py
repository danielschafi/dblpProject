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
        #get incollections with keyword in title
        incollections = []
        #get inprocceedings with keyword in title
        inproceedings = []
        #get masterthesis with keyword in title
        masterthesi = self.getMasterThesis(kword=keyword,
                                           schoolsList=schools)
        #get proceedings with keyword in title
        proceedings = []
        #get www model with keyword in title
        wwws = []
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
                               + len(books)),
                "phdthesis": phdThesis,
                "publishers": publishers,
                "schools": schools,
                "series": series,
                "journals": journals,
                "articles": articles,
                "datas": datas,
                "masterthesi": masterthesi,
                "books": books
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