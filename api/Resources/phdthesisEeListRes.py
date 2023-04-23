"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.phdthesisEeListModel import PhdthesisEeListModel as PELM
from Models.phdthesisModel import PhdthesisModel
from Models.eeModel import EeModel
from pseudocode import create_response, getDelParser
import os

class PhdthesisEeListRes(Resource):

    def get(self, _id):
        #gets pelm with pelm.id = id from db
        pelm = PELM.get(_id)
        if pelm:
            return create_response(pelm.to_json(), 200)
        return create_response({"message":"PhdthesisEeList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        pelm = PELM(**data)
        if not PhdthesisModel.get(data["phdthesisid"]):
            return create_response({
                "message": "Phdthesis does not exist"
            }, 400)
        if not EeModel.get(data["eeid"]):
            return create_response({
                "message": "Ee does not exist"
            }, 400)
        
        pelm.save()
        return create_response({
            "message": "PELM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        pelm = PELM.get(_id)
        if not pelm:
            return create_response({
                "message": f"No PELM with ID={_id} found"
            }, 200)
        pelm.delete()
        return create_response({
            "message": f"PELM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("phdthesisid",
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