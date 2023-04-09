"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.publisherModel import PublisherModel
from pseudocode import create_response

class PublisherRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        publisher = PublisherModel.get(_id)
        if publisher:
            return create_response(publisher.to_json(), 200)
        return create_response({"message":"Publisher not found"}, 404)