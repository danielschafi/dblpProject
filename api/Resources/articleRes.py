"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from Models.articleModel import ArticleModel
from pseudocode import create_response, getDelParser
import os

class ArticleRes(Resource):

    def get(self, _id):
        #gets article with article.id = id from db
        article = ArticleModel.get(_id)
        if article:
            return create_response(article.to_json(), 200)
        return create_response({"message":"Article not found"}, 404)
    
    def post(self, _id):
      parser = getPoParser()
      
      #Gets Payload Data
      data = parser.parse_args()

      #If Payload does not contain password,
      #reject request
      if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
      del data["pw"]

      #Create new object and update relationships
      article = ArticleModel(**data)
      article.journalid = data["journalid"]
      article.getJournal()

      #Check relationships
      if not article.journal:
          return create_response(f"Journal with ID:\
                                  {article.journalid} not\
                                 found", 400)
      #save object to db 
      article.save()
      return create_response(article.to_json(), 201)
    
    def delete(self, _id):
        parser = getDelParser()
        data = parser.parse_args()
        if data["pw"] != os.environ["DBLP_API_PW"]:
          return create_response({"message": "Unauthorized"}, 401)
        del data["pw"]

        article = ArticleModel.get(_id)
        if not article:
            return create_response({
                "message": f"No article with ID={_id} found"
            }, 200)
        article.delete()
        return create_response({
            "message": f"Article with ID={_id} deleted"
        }, 200)



def getPoParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("title",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("number",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pages",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("url",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("year",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("key",
                       type=str,
                       required=True,
                       help="This field cannot be left blank")
    parser.add_argument("journalid",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("pw",
                        type=str,
                        )
    return parser