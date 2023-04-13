"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.articleAuthorListModel import ArticleAuthorListModel as AALM
from pseudocode import create_response

class ArticleAuthorListRes(Resource):

    def get(self, _id):
        #gets aalm with aalm.id = id from db
        aalm = AALM.get(_id)
        if aalm:
            return create_response(aalm.to_json(), 200)
        return create_response({"message":"ArticleAuthorList not found"}, 404)