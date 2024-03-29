"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.bookModel import BookModel
from Models.schoolModel import SchoolModel
from Models.publisherModel import PublisherModel
from Models.seriesModel import SeriesModel
from pseudocode import create_response, getDelParser
import os

class BookRes(Resource):

    def get(self, _id):
        #gets book with book.id = id from db
        book = BookModel.get(_id)
        if book:
            return create_response(book.to_json(), 200)
        return create_response({"message":"Book not found"}, 404)
    
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
      book = BookModel(**data)

      school = SchoolModel.get(data["schoolid"])
      publisher = PublisherModel.get(data["publisherid"])
      series = SeriesModel.get(data["seriesid"])


      #Check relationships
      if not school:
          return create_response({
              "message":f"School with ID={data['schoolid']} not found"
              }, 400)
          
      if not publisher:
          return create_response({
              "message":f"Publisher with ID={data['publisherid']} not found"
              }, 400)

      if not series:
          return create_response({
              "message":f"Series with ID={data['seriesid']} not found"
              }, 400)
      #save object to db 
      book.save()
      return create_response(book.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        book = BookModel.get(_id)
        if not book:
            return create_response({
                "message": f"No book with ID={_id} found"
            }, 200)
        book.delete()
        return create_response({
            "message": f"Book with ID={_id} deleted"
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
    parser.add_argument("note",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("volume",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pages",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("isbn",
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