"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.schoolModel import SchoolModel
from pseudocode import create_response

class SchoolRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        school = SchoolModel.get(_id)
        if school:
            return create_response(school.to_json(), 200)
        return create_response({"message":"School not found"}, 404)