"""
Author: Daniel Schafhäutle
created: May 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.seriesModel import SeriesModel
from pseudocode import create_response, getDelParser
import os

class SeriesRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        series = SeriesModel.get(_id)
        if series:
            return create_response(series.to_json(), 200)
        return create_response({"message":"Series not found"}, 404)
    
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
      series = SeriesModel(**data)

      #save object to db 
      series.save()
      return create_response(series.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        series = SeriesModel.get(_id)
        if not series:
            return create_response({
                "message": f"No series with ID={_id} found"
            }, 200)
        series.delete()
        return create_response({
            "message": f"Series with ID={_id} deleted"
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