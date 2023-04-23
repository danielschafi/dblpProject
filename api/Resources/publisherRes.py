"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.publisherModel import PublisherModel
from pseudocode import create_response, getDelParser
import os

class PublisherRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        publisher = PublisherModel.get(_id)
        if publisher:
            return create_response(publisher.to_json(), 200)
        return create_response({"message":"Publisher not found"}, 404)
    
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
      publisher = PublisherModel(**data)

      #save object to db 
      publisher.save()
      return create_response(publisher.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        publisher = PublisherModel.get(_id)
        if not publisher:
            return create_response({
                "message": f"No publisher with ID={_id} found"
            }, 200)
        publisher.delete()
        return create_response({
            "message": f"Publisher with ID={_id} deleted"
        }, 200)



def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("name",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser