"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.proceedingsEeListModel import ProceedingsEeListModel as PLM
from Models.proceedingsModel import ProceedingsModel
from Models.eeModel import EeModel
from pseudocode import create_response, getDelParser
import os

class ProceedingsEeListRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        plm = PLM.get(_id)
        if plm:
            return create_response(plm.to_json(), 200)
        return create_response({"message":"ProceedingsEeList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        plm = PLM(**data)
        if not ProceedingsModel.get(data["proceedingsid"]):
            return create_response({
                "message": "Proceedings does not exist"
            }, 400)
        if not EeModel.get(data["eeid"]):
            return create_response({
                "message": "Ee does not exist"
            }, 400)
        
        plm.save()
        return create_response({
            "message": "PELM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        plm = PLM.get(_id)
        if not plm:
            return create_response({
                "message": f"No PELM with ID={_id} found"
            }, 200)
        plm.delete()
        return create_response({
            "message": f"PELM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("proceedingsid",
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