"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.eeTypeModel import EeTypeModel
from pseudocode import create_response, getDelParser
import os

class EeTypeRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        eeType = EeTypeModel.get(_id)
        if eeType:
            return create_response(eeType.to_json(), 200)
        return create_response({"message":"eeType not found"}, 404)
    
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
      eeType = EeTypeModel(**data)

      #save object to db 
      eeType.save()
      return create_response(eeType.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        eeType = EeTypeModel.get(_id)
        if not eeType:
            return create_response({
                "message": f"No EeType with ID={_id} found"
            }, 200)
        eeType.delete()
        return create_response({
            "message": f"EeType with ID={_id} deleted"
        }, 200)



def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("type",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser