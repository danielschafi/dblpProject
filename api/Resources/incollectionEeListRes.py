"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.incollectionEeListModel import IncollectionEeListModel as IELM
from pseudocode import create_response

class IncollectionEeListRes(Resource):

    def get(self, _id):
        #gets IELM with ielm.id = id from db
        ielm = IELM.get(_id)
        if ielm:
            return create_response(ielm.to_json(), 200)
        return create_response({"message":"IncollectionEeList not found"}, 404)