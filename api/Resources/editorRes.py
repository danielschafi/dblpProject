"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.editorModel import EditorModel
from pseudocode import create_response

class EditorRes(Resource):

    def get(self, _id):
        #gets author with author.id = id from db
        editor = EditorModel.get(_id)
        if editor:
            return create_response(editor.to_json(), 200)
        return create_response({"message":"Editor not found"}, 404)