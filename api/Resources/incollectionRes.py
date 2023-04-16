"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.incollectionModel import IncollectionModel
from pseudocode import create_response

class IncollectionRes(Resource):

    def get(self, _id):
        #gets incollection with incollection.id = id from db
        incollection = IncollectionModel.get(_id)
        if incollection:
            return create_response(incollection.to_json(), 200)
        return create_response({"message":"Incollection not found"}, 404)