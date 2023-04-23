"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.dataAuthorListModel import DataAuthorListModel as DALM
from Models.dataModel import DataModel
from Models.authorModel import AuthorModel
from pseudocode import create_response, getDelParser
import os

class DataAuthorListRes(Resource):

    def get(self, _id):
        #gets DALM with DALM.id = id from db
        dalm = DALM.get(_id)
        if dalm:
            return create_response(dalm.to_json(), 200)
        return create_response({"message":"DataAutohrList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        dalm = DALM(**data)
        if not DataModel.get(data["dataid"]):
            return create_response({
                "message": "Data does not exist"
            }, 400)
        if not AuthorModel.get(data["authorid"]):
            return create_response({
                "message": "Author does not exist"
            }, 400)
        
        dalm.save()
        return create_response({
            "message": "DALM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        dalm = DALM.get(_id)
        if not dalm:
            return create_response({
                "message": f"No DALM with ID={_id} found"
            }, 200)
        dalm.delete()
        return create_response({
            "message": f"DALM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("dataid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("authorid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser