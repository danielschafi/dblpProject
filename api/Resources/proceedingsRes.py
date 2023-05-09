"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.proceedingsModel import ProceedingsModel
from Models.publisherModel import PublisherModel
from Models.seriesModel import SeriesModel
from pseudocode import create_response, getDelParser
import os

class ProceedingsRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        proceedings = ProceedingsModel.get(_id)
        if proceedings:
            return create_response(proceedings.to_json(), 200)
        return create_response({"message":"Proceedings not found"}, 404)

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
      proceedings = ProceedingsModel(**data)

      #Check relationships      
      publisher = PublisherModel.get(data["publisherid"])
      series = SeriesModel.get(data["seriesid"])


      if not publisher:
          return create_response({
              "message":f"Publisher with ID={data['publisherid']} not found"
              }, 400)
          
      if not series:
          return create_response({
              "message":f"SEries with ID={data['seriesid']} not found"
              }, 400)
      #save object to db 
      proceedings.save()
      return create_response(proceedings.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        proceedings = ProceedingsModel.get(_id)
        if not proceedings:
            return create_response({
                "message": f"No proceedings with ID={_id} found"
            }, 200)
        proceedings.delete()
        return create_response({
            "message": f"Proceedings with ID={_id} deleted"
        }, 200)



def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("isbn",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("year",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("url",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("key",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("booktitle",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("title",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("volume",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("publisherid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("seriesid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser