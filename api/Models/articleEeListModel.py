"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class ArticleEeListModel(db.Model):

    __tablename__ = "articleeelist"
    id = db.Column(db.Integer, primary_key=True)
    eeid = db.Column(db.Integer, db.ForeignKey("ee.id"))
    ee = db.relationship("EeModel")

    articleid = db.Column(db.Integer, db.ForeignKey("article.id"))
    article = db.relationship("ArticleModel")


    def __init__(self, _id, eeid, articleid):
        self.id = _id
        self.eeid = eeid
        self.articleid = articleid

    def to_json(self):
        return {self.id: {
            "ee": self.ee.to_json(),
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
    def getByEeId(cls, myEeId):
        return cls.query.filter_by(eeid=myEeId).all()
    
    @classmethod
    def getByArticleId(cls, myProceId):
        return cls.query.filter_by(articleid=myProceId).all()