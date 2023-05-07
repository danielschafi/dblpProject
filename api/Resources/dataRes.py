"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.dataModel import DataModel
from pseudocode import create_response, getDelParser
import os

class DataRes(Resource):

    def get(self, _id):
        #gets data with data.id = id from db
        data = DataModel.get(_id)
        if data:
            return create_response(data.to_json(), 200)
        return create_response({"message":"Data not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        dataObj = DataModel(**data)
        
        dataObj.save()
        return create_response({
            "message": "Data created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        dataObj = DataModel.get(_id)
        if not dataObj:
            return create_response({
                "message": f"No data with ID={_id} found"
            }, 200)
        dataObj.delete()
        return create_response({
            "message": f"Data with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("crossref",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("title",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("note",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("number",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("month",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("year",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("key",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser