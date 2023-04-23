"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.masterthesisEeListModel import MasterthesisEeListModel as MELM
from Models.masterthesisModel import MasterthesisModel
from Models.eeModel import EeModel
from pseudocode import create_response, getDelParser
import os

class MasterthesisEeListRes(Resource):

    def get(self, _id):
        #gets melm with melm.id = id from db
        melm = MELM.get(_id)
        if melm:
            return create_response(melm.to_json(), 200)
        return create_response({"message":"MasterthesisEeList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        melm = MELM(**data)
        if not MasterthesisModel.get(data["masterthesisid"]):
            return create_response({
                "message": "Masterthesis does not exist"
            }, 400)
        if not EeModel.get(data["eeid"]):
            return create_response({
                "message": "Ee does not exist"
            }, 400)
        
        melm.save()
        return create_response({
            "message": "MELM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        melm = MELM.get(_id)
        if not melm:
            return create_response({
                "message": f"No MELM with ID={_id} found"
            }, 200)
        melm.delete()
        return create_response({
            "message": f"MELM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("masterthesisid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("eeid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser
