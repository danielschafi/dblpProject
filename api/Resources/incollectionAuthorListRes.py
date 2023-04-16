"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.incollectionAuthorListModel import IncollectionAuthorListModel as IALM
from pseudocode import create_response

class IncollectionAuthorListRes(Resource):

    def get(self, _id):
        #gets IALM with ialm.id = id from db
        ialm = IALM.get(_id)
        if ialm:
            return create_response(ialm.to_json(), 200)
        return create_response({"message":"IncollectionAuthorlist not found"}, 404)