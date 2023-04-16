"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.dataModel import DataModel
from pseudocode import create_response

class DataRes(Resource):

    def get(self, _id):
        #gets data with data.id = id from db
        data = DataModel.get(_id)
        if data:
            return create_response(data.to_json(), 200)
        return create_response({"message":"Data not found"}, 404)