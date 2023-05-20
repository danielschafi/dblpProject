"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.authorModel import AuthorModel
from Models.articleAuthorListModel import ArticleAuthorListModel
from Models.bookAuthorListModel import BookAuthorListModel
from Models.dataAuthorListModel import DataAuthorListModel
from Models.incollectionAuthorListModel import IncollectionAuthorListModel
from Models.inproceedingsAuthorListModel import InproceedingsAuthorListModel
from Models.masterthesisAuthorListModel import MasterthesisAuthorListModel
from Models.wwwAuthorListModel import WwwAuthorListModel
from Models.phdthesisAuthorListModel import PhdthesisAuthorListModel
from Models.phdthesisModel import PhdthesisModel
from Models.publisherModel import PublisherModel
from Models.schoolModel import SchoolModel
from Models.seriesModel import SeriesModel
from pseudocode import create_response, getDelParser
import os



class RelationshipRes(Resource):

    #Tuple of all tables in DB
    TABLE_NAMES = (
    "author", "cite", "editor",
    "journal", "school", "publisher",
    "series", "proceedings", "inproceedings",
    "data", "masterthesis", "phdthesis",
    "incollection", "book", "www", "article",
    )


    def get(self):
        
        parser = getGetParser()
        data = parser.parse_args()
        table = data["table"]
        relations = None
        if table == self.TABLE_NAMES[0]:
            relations = RelationshipRes.getAuthorRel(data["id"])
        
        else:
            return create_response({"message":f"Table {data['table']} does not exist"}, 400)
        if relations:
            return create_response(relations, 200)
        return create_response({"message": f"The Node with table: {data['table']}"\
                                f" and id: {data['id']} does not exist"}, 404)

        
    
    @classmethod
    def getAuthorRel(cls, _id):
        #returns all Ids of Nodes as dict connected to this table with id. If return = None, Node does not exist
        author = AuthorModel.get(_id)
        if not author:
            return None
        returnValue = {}
        #getArticles
        articles = ArticleAuthorListModel.getByAuthorId(_id)
        articlesIds = []
        for article in articles:
            articlesIds.append(article.articleid)
        returnValue["article"] = articlesIds
        #get Books
        books = BookAuthorListModel.getByAuthorId(_id)
        booksIds = []
        for book in books:
            booksIds.append(book.bookid)
        returnValue["book"] = booksIds
        #Get Data
        datas = DataAuthorListModel.getByAuthorId(_id)
        dataIds = []
        for data in datas:
            dataIds.append(data.dataid)
        returnValue["data"] = dataIds
        #Get Incollection
        incollections = IncollectionAuthorListModel.getByAuthorId(_id)
        incollectionIds = []
        for incol in incollections:
            incollectionIds.append(incol.incollectionid)
        returnValue["incollection"] = incollectionIds
        #Get Inproceedings
        inproceedings = InproceedingsAuthorListModel.getByAuthorId(_id)
        inprocIds = []
        for inproc in inproceedings:
            inprocIds.append(inproc.inproceedingsid)
        returnValue["inproceedings"] = inprocIds
        #Get Masterthesis
        masterthesi = MasterthesisAuthorListModel.getByAuthorId(_id)
        mastIds = []
        for masterthesis in masterthesi:
            mastIds.append(masterthesis.id)
        returnValue["masterthesis"] = mastIds
        #Get PHDThesis
        phds = PhdthesisAuthorListModel.getByAuthorId(_id)
        phdIds = []
        for phd in phds:
            phdIds.append(phd.phdthesisid)
        returnValue["phdthesis"] = phdIds
        #Get www
        wwws = WwwAuthorListModel.getByAuthorId(_id)
        wwwIds = []
        for www in wwws:
            wwwIds.append(www.wwwid)
        returnValue["www"] = wwwIds
        return returnValue
        



def getGetParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("id",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("table",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    return parser