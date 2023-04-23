"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.wwwModel import WwwModel
from pseudocode import create_response, getDelParser
import os

class WwwRes(Resource):

    def get(self, _id):
        #gets www with www.id = id from db
        www = WwwModel.get(_id)
        if www:
            return create_response(www.to_json(), 200)
        return create_response({"message":"Www not found"}, 404)
    
    def post(self, _id):
      parser = getPoParser()
      
      #Gets Payload Data
      data = parser.parse_args()

      #If Payload does not contain password,
      #reject request
      if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
      del data["pw"]

      #Create new object and update relationships
      www = WwwModel(**data)

      #save object to db 
      www.save()
      return create_response(www.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        www = WwwModel.get(_id)
        if not www:
            return create_response({
                "message": f"No Www with ID={_id} found"
            }, 200)
        www.delete()
        return create_response({
            "message": f"Www with ID={_id} deleted"
        }, 200)



def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("crossref",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("title",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("note",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("url",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser