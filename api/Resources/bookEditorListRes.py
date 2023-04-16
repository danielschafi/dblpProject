"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.bookEditorListModel import BookEditorListModel as BELM
from pseudocode import create_response

class BookEditorListRes(Resource):

    def get(self, _id):
        #gets belm with belm.id = id from db
        belm = BELM.get(_id)
        if belm:
            return create_response(belm.to_json(), 200)
        return create_response({"message":"BookeEditorList not found"}, 404)