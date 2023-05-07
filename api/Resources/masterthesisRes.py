"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.masterthesisModel import MasterthesisModel
from Models.schoolModel import SchoolModel
from pseudocode import create_response, getDelParser
import os

class MasterthesisRes(Resource):

    def get(self, _id):
        #gets MT with mt.id = id from db
        mt = MasterthesisModel.get(_id)
        if mt:
            return create_response(mt.to_json(), 200)
        return create_response({"message":"Masterthesis not found"}, 404)
    
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
      masterthesis = MasterthesisModel(**data)

      school = SchoolModel.get(data["schoolid"])

      #Check relationships
      if not school:
          return create_response({
              "message":f"School with ID={data['schoolid']} not found"
              }, 400)
      #save object to db 
      masterthesis.save()
      return create_response(masterthesis.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        masterthesis = MasterthesisModel.get(_id)
        if not masterthesis:
            return create_response({
                "message": f"No masterthesis with ID={_id} found"
            }, 200)
        masterthesis.delete()
        return create_response({
            "message": f"Masterthesis with ID={_id} deleted"
        }, 200)



def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("title",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("note",
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
    parser.add_argument("schoolid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser