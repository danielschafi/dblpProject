"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.eeTypeModel import EeTypeModel
from pseudocode import create_response

class EeTypeRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        eeType = EeTypeModel.get(_id)
        if eeType:
            return create_response(eeType.to_json(), 200)
        return create_response({"message":"eeType not found"}, 404)