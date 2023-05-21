"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from pseudocode import create_response, getDelParser

import importlib
Models = importlib.import_module("Models")
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
        elif table == self.TABLE_NAMES[1]:
            relations = RelationshipRes.getCiteRel(data["id"])
        
        else:
            return create_response({"message":f"Table {data['table']} does not exist"}, 400)
        if relations:
            return create_response(relations, 200)
        return create_response({"message": f"The Node with table: {data['table']}"\
                                f" and id: {data['id']} does not exist"}, 404)

        
    
    @classmethod
    def getAuthorRel(cls, _id):
        #returns all Ids of Nodes as dict connected to this table with id. If return = None, Node does not exist
        author = Models.authorModel.AuthorModel.get(_id)
        if not author:
            return None
        returnValue = {}
        #getArticles
        articles = Models.ArticleAuthorListModel.getByAuthorId(_id)
        articlesIds = []
        for article in articles:
            articlesIds.append(article.articleid)
        returnValue["article"] = articlesIds
        #get Books
        books = Models.bookAuthorListModel.BookAuthorListModel.getByAuthorId(_id)
        booksIds = []
        for book in books:
            booksIds.append(book.bookid)
        returnValue["book"] = booksIds
        #Get Data
        datas = Models.DataAuthorListModel.getByAuthorId(_id)
        dataIds = []
        for data in datas:
            dataIds.append(data.dataid)
        returnValue["data"] = dataIds
        #Get Incollection
        incollections = Models.IncollectionAuthorListModel.getByAuthorId(_id)
        incollectionIds = []
        for incol in incollections:
            incollectionIds.append(incol.incollectionid)
        returnValue["incollection"] = incollectionIds
        #Get Inproceedings
        inproceedings = Models.InproceedingsAuthorListModel.getByAuthorId(_id)
        inprocIds = []
        for inproc in inproceedings:
            inprocIds.append(inproc.inproceedingsid)
        returnValue["inproceedings"] = inprocIds
        #Get Masterthesis
        masterthesi = Models.MasterthesisAuthorListModel.getByAuthorId(_id)
        mastIds = []
        for masterthesis in masterthesi:
            mastIds.append(masterthesis.id)
        returnValue["masterthesis"] = mastIds
        #Get PHDThesis
        phds = Models.PhdthesisAuthorListModel.getByAuthorId(_id)
        phdIds = []
        for phd in phds:
            phdIds.append(phd.phdthesisid)
        returnValue["phdthesis"] = phdIds
        #Get www
        wwws = Models.WwwAuthorListModel.getByAuthorId(_id)
        wwwIds = []
        for www in wwws:
            wwwIds.append(www.wwwid)
        returnValue["www"] = wwwIds
        return returnValue

    @classmethod    
    def getCiteRel(cls, _id):
        cite = Models.citeModel.CiteModel.get(_id)
        if not cite:
            return None
        returnValue = {}
        #getArticles
        articles = Models.ArticleAuthorListModel.getByAuthorId(_id)
        articlesIds = []
        for article in articles:
            articlesIds.append(article.articleid)
        returnValue["article"] = articlesIds
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