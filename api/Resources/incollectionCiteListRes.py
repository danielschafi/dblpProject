"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.incollectionCiteListModel import IncollectionCiteListModel as ICLM
from Models.incollectionModel import IncollectionModel
from Models.citeModel import CiteModel
from pseudocode import create_response, getDelParser
import os

class IncollectionCiteListRes(Resource):

    def get(self, _id):
        #gets ICLM with iclm.id = id from db
        iclm = ICLM.get(_id)
        if iclm:
            return create_response(iclm.to_json(), 200)
        return create_response({"message":"IncollectionCiteList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        iclm = ICLM(**data)
        if not IncollectionModel.get(data["incollectionid"]):
            return create_response({
                "message": "Incollection does not exist"
            }, 400)
        if not CiteModel.get(data["citeid"]):
            return create_response({
                "message": "Cite does not exist"
            }, 400)
        
        iclm.save()
        return create_response({
            "message": "ICLM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        iclm = ICLM.get(_id)
        if not iclm:
            return create_response({
                "message": f"No ICLM with ID={_id} found"
            }, 200)
        iclm.delete()
        return create_response({
            "message": f"ICLM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("incollectionid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("citeid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser