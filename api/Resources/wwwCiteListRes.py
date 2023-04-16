"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.wwwCiteListModel import WwwCiteListModel as WCLM
from pseudocode import create_response

class WwwCiteListRes(Resource):

    def get(self, _id):
        #gets wclm with wclm.id = id from db
        wclm = WCLM.get(_id)
        if wclm:
            return create_response(wclm.to_json(), 200)
        return create_response({"message":"WwwCiteList not found"}, 404)