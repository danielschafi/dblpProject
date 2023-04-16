"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.inproceedingsEeListModel import InproceedingsEeListModel as IELM
from pseudocode import create_response

class InproceedingsEeListRes(Resource):

    def get(self, _id):
        #gets ielm with ielm.id = id from db
        ielm = IELM.get(_id)
        if ielm:
            return create_response(ielm.to_json(), 200)
        return create_response({"message":"InproceedingsEeList not found"}, 404)