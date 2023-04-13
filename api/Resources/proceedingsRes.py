"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.proceedingsModel import ProceedingsModel
from pseudocode import create_response

class ProceedingsRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        proceedings = ProceedingsModel.get(_id)
        if proceedings:
            return create_response(proceedings.to_json(), 200)
        return create_response({"message":"Proceedings not found"}, 404)
