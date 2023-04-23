"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.masterthesisAuthorListModel import MasterthesisAuthorListModel as MALM
from Models.masterthesisModel import MasterthesisModel
from Models.authorModel import AuthorModel
from pseudocode import create_response, getDelParser
import os

class MasterthesisAuthorListRes(Resource):

    def get(self, _id):
        #gets malm with malm.id = id from db
        malm = MALM.get(_id)
        if malm:
            return create_response(malm.to_json(), 200)
        return create_response({"message":"MasterthesisAuthorList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        malm = MALM(**data)
        if not MasterthesisModel.get(data["masterthesisid"]):
            return create_response({
                "message": "Masterthesis does not exist"
            }, 400)
        if not AuthorModel.get(data["authorid"]):
            return create_response({
                "message": "Author does not exist"
            }, 400)
        
        malm.save()
        return create_response({
            "message": "MALM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        malm = MALM.get(_id)
        if not malm:
            return create_response({
                "message": f"No MALM with ID={_id} found"
            }, 200)
        malm.delete()
        return create_response({
            "message": f"MALM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("masterthesisid",
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