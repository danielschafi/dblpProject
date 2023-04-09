"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.eeModel import EeModel
from pseudocode import create_response

class EeRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        ee = EeModel.get(_id)
        if ee:
            return create_response(ee.to_json(), 200)
        return create_response({"message":"EE not found"}, 404)