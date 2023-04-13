"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.articleEeListModel import ArticleEeListModel as AELM
from pseudocode import create_response

class ArticleEeListRes(Resource):

    def get(self, _id):
        #gets aelm with aelm.id = id from db
        aelm = AELM.get(_id)
        if aelm:
            return create_response(aelm.to_json(), 200)
        return create_response({"message":"ArticleEeList not found"}, 404)