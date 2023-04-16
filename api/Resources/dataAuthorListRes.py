"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.dataAuthorListModel import DataAuthorListModel as DALM
from pseudocode import create_response

class DataAuthorListRes(Resource):

    def get(self, _id):
        #gets DALM with DALM.id = id from db
        dalm = DALM.get(_id)
        if dalm:
            return create_response(dalm.to_json(), 200)
        return create_response({"message":"DataAutohrList not found"}, 404)