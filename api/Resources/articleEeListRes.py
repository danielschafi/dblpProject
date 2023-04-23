"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.articleEeListModel import ArticleEeListModel as AELM
from Models.articleModel import ArticleModel
from Models.eeModel import EeModel
from pseudocode import create_response, getDelParser
import os

class ArticleEeListRes(Resource):

    def get(self, _id):
        #gets aelm with aelm.id = id from db
        aelm = AELM.get(_id)
        if aelm:
            return create_response(aelm.to_json(), 200)
        return create_response({"message":"ArticleEeList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        aelm = AELM(**data)
        if not ArticleModel.get(data["articleid"]):
            return create_response({
                "message": "Article does not exist"
            }, 400)
        if not EeModel.get(data["eeid"]):
            return create_response({
                "message": "Author does not exist"
            }, 400)
        
        aelm.save()
        return create_response({
            "message": "AELM created"
        }, 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        aelm = AELM.get(_id)
        if not aelm:
            return create_response({
                "message": f"No AELM with ID={_id} found"
            }, 200)
        aelm.delete()
        return create_response({
            "message": f"AELM with ID={_id} deleted"
        }, 200)
    

    
def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("articleid",
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
