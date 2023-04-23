"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.phdthesisModel import PhdthesisModel
from Models.publisherModel import PublisherModel
from Models.schoolModel import SchoolModel
from pseudocode import create_response, getDelParser
import os

class PhdthesisRes(Resource):

    def get(self, _id):
        #gets phdthesis with phdthesis.id = id from db
        phdthesis = PhdthesisModel.get(_id)
        if phdthesis:
            return create_response(phdthesis.to_json(), 200)
        return create_response({"message":"Phdthesis not found"}, 404)
    
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
      phd = PhdthesisModel(**data)

      school = SchoolModel.get(data["schoolid"])

      #Check relationships
      if not school:
          return create_response({
              "message":f"School with ID={data['schoolid']} not found"
              }, 400)
      
      publisher = PublisherModel.get(data["publisherid"])

      if not publisher:
          return create_response({
              "message":f"Publisher with ID={data['publisherid']} not found"
              }, 400)
      #save object to db 
      phd.save()
      return create_response(phd.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        phd = PhdthesisModel.get(_id)
        if not phd:
            return create_response({
                "message": f"No phdthesis with ID={_id} found"
            }, 200)
        phd.delete()
        return create_response({
            "message": f"Phdthesis with ID={_id} deleted"
        }, 200)



def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("series",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("title",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("isbn",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("note",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("number",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pages",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("volume",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("year",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("month",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("schoolid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("publisherid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser