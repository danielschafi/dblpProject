"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.phdthesisModel import PhdthesisModel
from pseudocode import create_response

class PhdthesisRes(Resource):

    def get(self, _id):
        #gets phdthesis with phdthesis.id = id from db
        phdthesis = PhdthesisModel.get(_id)
        if phdthesis:
            return create_response(phdthesis.to_json(), 200)
        return create_response({"message":"Phdthesis not found"}, 404)