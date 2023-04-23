"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.journalModel import JournalModel
from pseudocode import create_response, getDelParser
import os

class JournalRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        journal = JournalModel.get(_id)
        if journal:
            return create_response(journal.to_json(), 200)
        return create_response({"message":"Journal not found"}, 404)
    
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
      journal = JournalModel(**data)

      #save object to db 
      journal.save()
      return create_response(journal.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        journal = JournalModel.get(_id)
        if not journal:
            return create_response({
                "message": f"No Journal with ID={_id} found"
            }, 200)
        journal.delete()
        return create_response({
            "message": f"Journal with ID={_id} deleted"
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