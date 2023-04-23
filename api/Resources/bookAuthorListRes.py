"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.bookAuthorListModel import BookAuthorListModel as BALM
from Models.authorModel import AuthorModel
from Models.bookModel import BookModel
from pseudocode import create_response, getDelParser
import os

class BookAuthorListRes(Resource):

    def get(self, _id):
        #gets balm with balm.id = id from db
        balm = BALM.get(_id)
        if balm:
            return create_response(balm.to_json(), 200)
        return create_response({"message":"BookAuthorList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        balm = BALM(**data)
        if not BookModel.get(data["bookid"]):
            return create_response({
                "message": "Book does not exist"
            }, 400)
        if not AuthorModel.get(data["authorid"]):
            return create_response({
                "message": "Author does not exist"
            }, 400)
        
        balm.save()
        return create_response({
            "message": "BALM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        balm = BALM.get(_id)
        if not balm:
            return create_response({
                "message": f"No BALM with ID={_id} found"
            }, 200)
        balm.delete()
        return create_response({
            "message": f"BALM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("bookid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("authorid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser