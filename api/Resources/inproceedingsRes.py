"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.inproceedingsModel import InproceedingsModel
from pseudocode import create_response, getDelParser
import os

class InproceedingsRes(Resource):

    def get(self, _id):
        #gets inproceedings with inproceedings.id = id from db
        inproceedings = InproceedingsModel.get(_id)
        if inproceedings:
            return create_response(inproceedings.to_json(), 200)
        return create_response({"message":"Inproceedings not found"}, 404)
    
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
      inproceedings = InproceedingsModel(**data)

      #save object to db 
      inproceedings.save()
      return create_response(inproceedings.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        inproeedings = InproceedingsModel.get(_id)
        if not inproeedings:
            return create_response({
                "message": f"No Inproceedings with ID={_id} found"
            }, 200)
        inproeedings.delete()
        return create_response({
            "message": f"Inproceedings with ID={_id} deleted"
        }, 200)



def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("title",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("year",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("crossref",
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
    parser.add_argument("pages",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument("pw",
                        type=str,
                        )
    return parser