"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.bookModel import BookModel
from pseudocode import create_response

class BookRes(Resource):

    def get(self, _id):
        #gets book with book.id = id from db
        book = BookModel.get(_id)
        if book:
            return create_response(book.to_json(), 200)
        return create_response({"message":"Book not found"}, 404)