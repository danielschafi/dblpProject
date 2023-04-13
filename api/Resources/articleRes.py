"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource
from Models.articleModel import ArticleModel
from pseudocode import create_response

class ArticleRes(Resource):

    def get(self, _id):
        #gets article with article.id = id from db
        article = ArticleModel.get(_id)
        if article:
            return create_response(article.to_json(), 200)
        return create_response({"message":"Article not found"}, 404)