"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.bookEditorListModel import BookEditorListModel as BELM
from Models.bookModel import BookModel
from Models.editorModel import EditorModel
from pseudocode import create_response, getDelParser
import os

class BookEditorListRes(Resource):

    def get(self, _id):
        #gets belm with belm.id = id from db
        belm = BELM.get(_id)
        if belm:
            return create_response(belm.to_json(), 200)
        return create_response({"message":"BookeEditorList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        belm = BELM(**data)
        if not BookModel.get(data["bookid"]):
            return create_response({
                "message": "Book does not exist"
            }, 400)
        if not EditorModel.get(data["editorid"]):
            return create_response({
                "message": "Author does not exist"
            }, 400)
        
        belm.save()
        return create_response({
            "message": "BELM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        belm = BELM.get(_id)
        if not belm:
            return create_response({
                "message": f"No BELM with ID={_id} found"
            }, 200)
        belm.delete()
        return create_response({
            "message": f"BELM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("bookid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("editorid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser