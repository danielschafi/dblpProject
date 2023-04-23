"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class ArticleAuthorListModel(db.Model):

    __tablename__ = "articleauthorlist"
    id = db.Column(db.Integer, primary_key=True)

    authorid = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("AuthorModel")

    articleid = db.Column(db.Integer, db.ForeignKey("article.id"))
    article = db.relationship("ArticleModel")


    def __init__(self, authorid, articleid):
        self.authorid = authorid
        self.articleid = articleid

    def to_json(self):
        return {self.id: {
            "author": self.author.to_json(),
            "article": self.article.to_json()
        }}
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def get(cls, myId):
        #Get always filters by primary_key
        #None if id not found
        return cls.query.filter_by(id=myId).first()
    
    @classmethod
    def getByAuthorId(cls, myAuthorId):
        return cls.query.filter_by(authorid=myAuthorId).all()
    
    @classmethod
    def getByArticleId(cls, myarthicleId):
        return cls.query.filter_by(articleid=myarthicleId).all()