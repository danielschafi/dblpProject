"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.wwwModel import WwwModel
from pseudocode import create_response

class WwwRes(Resource):

    def get(self, _id):
        #gets www with www.id = id from db
        www = WwwModel.get(_id)
        if www:
            return create_response(www.to_json(), 200)
        return create_response({"message":"Www not found"}, 404)