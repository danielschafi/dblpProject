"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.incollectionModel import IncollectionModel
from pseudocode import create_response, getDelParser
import os

class IncollectionRes(Resource):

    def get(self, _id):
        #gets incollection with incollection.id = id from db
        incollection = IncollectionModel.get(_id)
        if incollection:
            return create_response(incollection.to_json(), 200)
        return create_response({"message":"Incollection not found"}, 404)
    
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
      incollection = IncollectionModel(**data)

      #save object to db 
      incollection.save()
      return create_response(incollection.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        incollection = IncollectionModel.get(_id)
        if not incollection:
            return create_response({
                "message": f"No Incollection with ID={_id} found"
            }, 200)
        incollection.delete()
        return create_response({
            "message": f"Incollection with ID={_id} deleted"
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
    parser.add_argument("pages",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("booktitle",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("url",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("year",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("key",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser