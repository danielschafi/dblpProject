"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.authorModel import AuthorModel
from pseudocode import create_response

class AuthorRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        author = AuthorModel.get(_id)
        if author:
            return create_response(author.to_json(), 200)
        return create_response({"message":"Author not found"}, 404)