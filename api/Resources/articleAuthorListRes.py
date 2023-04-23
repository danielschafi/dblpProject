"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.articleAuthorListModel import ArticleAuthorListModel as AALM
from Models.articleModel import ArticleModel
from Models.authorModel import AuthorModel
from pseudocode import create_response
import os

class ArticleAuthorListRes(Resource):

    def get(self, _id):
        #gets aalm with aalm.id = id from db
        aalm = AALM.get(_id)
        if aalm:
            return create_response(aalm.to_json(), 200)
        return create_response({"message":"ArticleAuthorList not found"}, 404)
    
    def post(self, _id):
        parser = getPoParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        aalm = AALM(**data)
        if not ArticleModel.get(data["articleid"]):
            return create_response({
                "message": "Article does not exist"
            }, 400)
        if not AuthorModel.get(data["authorid"]):
            return create_response({
                "message": "Author does not exist"
            }, 400)
        
        aalm.save()
        return create_response({
            "message": "AALM created"
        }, 201)


def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("articleid",
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