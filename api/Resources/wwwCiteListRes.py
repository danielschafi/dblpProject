"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.wwwCiteListModel import WwwCiteListModel as WCLM
from Models.wwwModel import WwwModel
from Models.citeModel import CiteModel
from pseudocode import create_response, getDelParser
import os

class WwwCiteListRes(Resource):

    def get(self, _id):
        #gets wclm with wclm.id = id from db
        wclm = WCLM.get(_id)
        if wclm:
            return create_response(wclm.to_json(), 200)
        return create_response({"message":"WwwCiteList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        wclm = WCLM(**data)
        if not WwwModel.get(data["wwwid"]):
            return create_response({
                "message": "Www does not exist"
            }, 400)
        if not CiteModel.get(data["citeid"]):
            return create_response({
                "message": "Cite does not exist"
            }, 400)
        
        wclm.save()
        return create_response({
            "message": "WCLM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        wclm = WCLM.get(_id)
        if not wclm:
            return create_response({
                "message": f"No WCLM with ID={_id} found"
            }, 200)
        wclm.delete()
        return create_response({
            "message": f"WCLM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("wwwid",
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