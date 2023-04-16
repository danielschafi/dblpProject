"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.masterthesisModel import MasterthesisModel
from pseudocode import create_response

class MasterthesisRes(Resource):

    def get(self, _id):
        #gets MT with mt.id = id from db
        mt = MasterthesisModel.get(_id)
        if mt:
            return create_response(mt.to_json(), 200)
        return create_response({"message":"Masterthesis not found"}, 404)