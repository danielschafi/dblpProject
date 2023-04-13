"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.bookAuthorListModel import BookAuthorListModel as BALM
from pseudocode import create_response

class BookAuthorListRes(Resource):

    def get(self, _id):
        #gets balm with balm.id = id from db
        balm = BALM.get(_id)
        if balm:
            return create_response(balm.to_json(), 200)
        return create_response({"message":"BookAuthorList not found"}, 404)