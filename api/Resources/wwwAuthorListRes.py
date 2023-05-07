"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.wwwAuthorListModel import WwwAuthorListModel as WALR
from Models.wwwModel import WwwModel
from Models.authorModel import AuthorModel
from pseudocode import create_response, getDelParser
import os

class WwwAuthorListRes(Resource):

    def get(self, _id):
        #gets walr with walr.id = id from db
        walr = WALR.get(_id)
        if walr:
            return create_response(walr.to_json(), 200)
        return create_response({"message":"WwwAuthorList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        walr = WALR(**data)
        if not WwwModel.get(data["wwwid"]):
            return create_response({
                "message": "Www does not exist"
            }, 400)
        if not AuthorModel.get(data["authorid"]):
            return create_response({
                "message": "Author does not exist"
            }, 400)
        
        walr.save()
        return create_response({
            "message": "WALR created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        walr = WALR.get(_id)
        if not walr:
            return create_response({
                "message": f"No WALR with ID={_id} found"
            }, 200)
        walr.delete()
        return create_response({
            "message": f"WALR with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("wwwid",
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