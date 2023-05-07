"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.dataEeListModel import DataEeListModel as DELM
from Models.dataModel import DataModel
from Models.eeModel import EeModel
from pseudocode import create_response, getDelParser
import os

class DataAuthorListRes(Resource):

    def get(self, _id):
        #gets DALM with DALM.id = id from db
        dalm = DELM.get(_id)
        if dalm:
            return create_response(dalm.to_json(), 200)
        return create_response({"message":"DataEeList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        dalm = DELM(**data)
        if not DataModel.get(data["dataid"]):
            return create_response({
                "message": "Data does not exist"
            }, 400)
        if not EeModel.get(data["eeid"]):
            return create_response({
                "message": "Ee does not exist"
            }, 400)
        
        dalm.save()
        return create_response({
            "message": "DELM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        delm = DELM.get(_id)
        if not delm:
            return create_response({
                "message": f"No DELM with ID={_id} found"
            }, 200)
        delm.delete()
        return create_response({
            "message": f"DELM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("dataid",
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