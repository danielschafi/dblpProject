"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.incollectionCiteListModel import IncollectionCiteListModel as ICLM
from pseudocode import create_response

class IncollectionCiteListRes(Resource):

    def get(self, _id):
        #gets ICLM with iclm.id = id from db
        iclm = ICLM.get(_id)
        if iclm:
            return create_response(iclm.to_json(), 200)
        return create_response({"message":"IncollectionCiteList not found"}, 404)