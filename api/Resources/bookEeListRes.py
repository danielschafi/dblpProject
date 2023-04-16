"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.bookEeListModel import BookEeListModel as BEELM
from pseudocode import create_response

class BookEeListRes(Resource):

    def get(self, _id):
        #gets belm with belm.id = id from db
        beelm = BEELM.get(_id)
        if beelm:
            return create_response(beelm.to_json(), 200)
        return create_response({"message":"BookEeList not found"}, 404)