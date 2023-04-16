"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.inproceedingsModel import InproceedingsModel
from pseudocode import create_response

class InproceedingsRes(Resource):

    def get(self, _id):
        #gets inproceedings with inproceedings.id = id from db
        inproceedings = InproceedingsModel.get(_id)
        if inproceedings:
            return create_response(inproceedings.to_json(), 200)
        return create_response({"message":"Inproceedings not found"}, 404)