"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.phdthesisEeListModel import PhdthesisEeListModel as PELM
from pseudocode import create_response

class PhdthesisEeListRes(Resource):

    def get(self, _id):
        #gets pelm with pelm.id = id from db
        pelm = PELM.get(_id)
        if pelm:
            return create_response(pelm.to_json(), 200)
        return create_response({"message":"PhdthesisEeList not found"}, 404)