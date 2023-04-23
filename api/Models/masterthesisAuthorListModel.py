"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class MasterthesisAuthorListModel(db.Model):

    __tablename__ = "masterthesisauthorlist"
    id = db.Column(db.Integer, primary_key=True)

    authorid = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("AuthorModel")

    masterthesisid = db.Column(db.Integer, db.ForeignKey("masterthesis.id"))
    masterthesis = db.relationship("MasterthesisModel")


    def __init__(self, authorid, masterthesisid):
        self.authorid = authorid
        self.masterthesisid = masterthesisid

    def to_json(self):
        return {self.id: {
            "author": self.author.to_json(),
            "masterthesis": self.masterthesis.to_json()
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
    def getByPhdthesisId(cls, myMasterthesisID):
        return cls.query.filter_by(masterthesisid=myMasterthesisID).all()