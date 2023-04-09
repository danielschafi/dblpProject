"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.proceedingsEeListModel import ProceedingsEeListModel as PLM
from pseudocode import create_response

class ProceedingsEeListRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        plm = PLM.get(_id)
        if plm:
            return create_response(plm.to_json(), 200)
        return create_response({"message":"Cite not found"}, 404)