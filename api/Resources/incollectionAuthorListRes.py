"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.incollectionAuthorListModel import IncollectionAuthorListModel as IALM
from Models.incollectionModel import IncollectionModel
from Models.authorModel import AuthorModel
from pseudocode import create_response, getDelParser
import os

class IncollectionAuthorListRes(Resource):

    def get(self, _id):
        #gets IALM with ialm.id = id from db
        ialm = IALM.get(_id)
        if ialm:
            return create_response(ialm.to_json(), 200)
        return create_response({"message":"IncollectionAuthorlist not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        ialm = IALM(**data)
        if not IncollectionModel.get(data["incollectionid"]):
            return create_response({
                "message": "Incollection does not exist"
            }, 400)
        if not AuthorModel.get(data["authorid"]):
            return create_response({
                "message": "Author does not exist"
            }, 400)
        
        ialm.save()
        return create_response({
            "message": "IALM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        ialm = IALM.get(_id)
        if not ialm:
            return create_response({
                "message": f"No IALM with ID={_id} found"
            }, 200)
        ialm.delete()
        return create_response({
            "message": f"IALM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("incollectionid",
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