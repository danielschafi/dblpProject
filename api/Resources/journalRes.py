"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.journalModel import JournalModel
from pseudocode import create_response

class JournalRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        journal = JournalModel.get(_id)
        if journal:
            return create_response(journal.to_json(), 200)
        return create_response({"message":"Journal not found"}, 404)