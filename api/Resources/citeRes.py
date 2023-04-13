"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.citeModel import CiteModel
from pseudocode import create_response

class CiteRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        cite = CiteModel.get(_id)
        if cite:
            return create_response(cite.to_json(), 200)
        return create_response({"message":"Cite not found"}, 404)