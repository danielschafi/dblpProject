"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.inproceedingsEeListModel import InproceedingsEeListModel as IELM
from Models.inproceedingsModel import InproceedingsModel
from Models.eeModel import EeModel
from pseudocode import create_response, getDelParser
import os

class InproceedingsEeListRes(Resource):

    def get(self, _id):
        #gets ielm with ielm.id = id from db
        ielm = IELM.get(_id)
        if ielm:
            return create_response(ielm.to_json(), 200)
        return create_response({"message":"InproceedingsEeList not found"}, 404)

    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        ielm = IELM(**data)
        if not InproceedingsModel.get(data["inproceedingsid"]):
            return create_response({
                "message": "Inproceedings does not exist"
            }, 400)
        if not EeModel.get(data["eeid"]):
            return create_response({
                "message": "Author does not exist"
            }, 400)
        
        ielm.save()
        return create_response({
            "message": "Ielm created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        ielm = IELM.get(_id)
        if not ielm:
            return create_response({
                "message": f"No IELM with ID={_id} found"
            }, 200)
        ielm.delete()
        return create_response({
            "message": f"IELM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("inproceedingsid",
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