"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.phdthesisAuthorListModel import PhdthesisAuthorListModel as PALM
from Models.phdthesisModel import PhdthesisModel
from Models.authorModel import AuthorModel
from pseudocode import create_response, getDelParser
import os

class PhdthesisAuthorListRes(Resource):

    def get(self, _id):
        parser = getGetParser()
        data = parser.parse_args()
        if data.get("authorId"):
            authors = PALM.getByAuthorId(data["authorId"])
            return_value = []
            for author in authors:
                return_value.append(author.to_json())
            return create_response(return_value, 200)
        #gets palm with palm.id = id from db
        palm = PALM.get(_id)
        if palm:
            return create_response(palm.to_json(), 200)
        return create_response({"message":"PhdthesisAuthorList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        palm = PALM(**data)
        if not PhdthesisModel.get(data["phdthesisid"]):
            return create_response({
                "message": "Phdthesis does not exist"
            }, 400)
        if not AuthorModel.get(data["authorid"]):
            return create_response({
                "message": "Author does not exist"
            }, 400)
        
        palm.save()
        return create_response({
            "message": "PALM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        palm = PALM.get(_id)
        if not palm:
            return create_response({
                "message": f"No PALM with ID={_id} found"
            }, 200)
        palm.delete()
        return create_response({
            "message": f"PALM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("phdthesisid",
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

def getGetParser():
    parser = reqparse.RequestParser()
    parser.add_argument("authorId",
                        type=str,)
    return parser