"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.incollectionEeListModel import IncollectionEeListModel as IELM
from Models.incollectionModel import IncollectionModel
from Models.eeModel import EeModel
from pseudocode import create_response, getDelParser
import os

class IncollectionEeListRes(Resource):

    def get(self, _id):
        #gets IELM with ielm.id = id from db
        ielm = IELM.get(_id)
        if ielm:
            return create_response(ielm.to_json(), 200)
        return create_response({"message":"IncollectionEeList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        ielm = IELM(**data)
        if not IncollectionModel.get(data["incollectionid"]):
            return create_response({
                "message": "Incollection does not exist"
            }, 400)
        if not EeModel.get(data["eeid"]):
            return create_response({
                "message": "Cite does not exist"
            }, 400)
        
        ielm.save()
        return create_response({
            "message": "IELM created"
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
    parser.add_argument("incollectionid",
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