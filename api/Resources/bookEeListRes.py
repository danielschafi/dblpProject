"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.bookEeListModel import BookEeListModel as BEELM
from Models.bookModel import BookModel
from Models.eeModel import EeModel
from pseudocode import create_response, getDelParser
import os

class BookEeListRes(Resource):

    def get(self, _id):
        #gets belm with belm.id = id from db
        beelm = BEELM.get(_id)
        if beelm:
            return create_response(beelm.to_json(), 200)
        return create_response({"message":"BookEeList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        beelm = BEELM(**data)
        if not BookModel.get(data["bookid"]):
            return create_response({
                "message": "Book does not exist"
            }, 400)
        if not EeModel.get(data["eeid"]):
            return create_response({
                "message": "Author does not exist"
            }, 400)
        
        beelm.save()
        return create_response({
            "message": "BEELM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        beelm = BEELM.get(_id)
        if not beelm:
            return create_response({
                "message": f"No BEELM with ID={_id} found"
            }, 200)
        beelm.delete()
        return create_response({
            "message": f"BEELM with ID={_id} deleted"
        }, 200)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("bookid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("eeid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser