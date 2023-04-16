"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.phdthesisAuthorListModel import PhdthesisAuthorListModel as PALM
from pseudocode import create_response

class PhdthesisAuthorListRes(Resource):

    def get(self, _id):
        #gets palm with palm.id = id from db
        palm = PALM.get(_id)
        if palm:
            return create_response(palm.to_json(), 200)
        return create_response({"message":"PhdthesisAuthorList not found"}, 404)