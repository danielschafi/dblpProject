"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.masterthesisEeListModel import MasterthesisEeListModel as MELM
from pseudocode import create_response

class MasterthesisEeListRes(Resource):

    def get(self, _id):
        #gets melm with melm.id = id from db
        melm = MELM.get(_id)
        if melm:
            return create_response(melm.to_json(), 200)
        return create_response({"message":"MasterthesisEeList not found"}, 404)