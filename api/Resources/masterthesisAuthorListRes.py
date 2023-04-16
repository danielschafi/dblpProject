"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.masterthesisAuthorListModel import MasterthesisAuthorListModel as MALM
from pseudocode import create_response

class MasterthesisAuthorListRes(Resource):

    def get(self, _id):
        #gets malm with malm.id = id from db
        malm = MALM.get(_id)
        if malm:
            return create_response(malm.to_json(), 200)
        return create_response({"message":"MasterthesisAuthorList not found"}, 404)