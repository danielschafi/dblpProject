"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.connectModel import ConnectModel
from pseudocode import create_response, getDelParser
import os

class ConnectRes(Resource):

    def get(self):
        #gets author with author.id = id from db
        parser = getGetParser()
        data = parser.parse_args()
        if data["tablename"] and data["id"]:
            connect = ConnectModel.get(**data)
            if connect:
                return create_response(connect.to_json(), 200)
            return create_response({"message":"Connect-Node not found"}, 404)
        connects = ConnectModel.getByOrderId(data["orderid"])
        returnValue = []
        for connect in connects:
            returnValue.append(connect.to_json())
        return create_response(returnValue, 200)
    
    def post(self):
      parser = getGetParser()
      
      #Gets Payload Data
      data = parser.parse_args()

      #Create new object and update relationships
      connect = ConnectModel(**data)

      #save object to db 
      connect.save()
      return create_response(connect.to_json(), 201)
    
    def delete(self):
        parser = getGetParser()
        data = parser.parse_args()
        connect = ConnectModel.get(**data)
        if not connect:
            return create_response({
                "message": f"No Connect-Node found"
            }, 200)
        connect.delete()
        return create_response({
            "message": f"Connect deleted"
        }, 200)

def getGetParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("orderid",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("tablename",
                        type=str,
                        )
    parser.add_argument("id",
                        type=str,
                        )
    return parser
