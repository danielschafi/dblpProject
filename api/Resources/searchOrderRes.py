"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.searchOrderModel import SearchOrderModel
from pseudocode import create_response, getDelParser
import os

class SearchOrderRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        searchOrder = SearchOrderModel.get(_id)
        if searchOrder:
            return create_response(searchOrder.to_json(), 200)
        return create_response({"message":"SearchOrder not found"}, 404)
    
    def post(self, _id):
      parser = getPoParser()
      
      #Gets Payload Data
      data = parser.parse_args()

      #Create new object and update relationships
      searchOrder = SearchOrderModel(**data)

      #save object to db 
      searchOrder.save()
      return create_response(searchOrder.to_json(), 201)
    
    def delete(self, _id):
        searchOrder = SearchOrderModel.get(_id)
        if not searchOrder:
            return create_response({
                "message": f"No searchOrder with ID={_id} found"
            }, 200)
        searchOrder.delete()
        return create_response({
            "message": f"SearchOrder with ID={_id} deleted"
        }, 200)



def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("keyword",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("start_node",
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument("email",
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument("max_distance",
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    return parser