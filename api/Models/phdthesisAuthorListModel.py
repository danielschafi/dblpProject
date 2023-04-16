"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class PhdthesisAuthorListModel(db.Model):

    __tablename__ = "phdthesisauthorlist"
    id = db.Column(db.Integer, primary_key=True)

    authorid = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("AuthorModel")

    phdthesisid = db.Column(db.Integer, db.ForeignKey("phdthesis.id"))
    phdthesis = db.relationship("PhdthesisModel")


    def __init__(self, _id, authorid, phdthesisid):
        self.id = _id
        self.authorid = authorid
        self.phdthesisid = phdthesisid

    def to_json(self):
        return {self.id: {
            "author": self.author.to_json(),
            "phdthesis": self.phdthesis.to_json()
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
    def getByPhdthesisId(cls, myPhdthesisId):
        return cls.query.filter_by(phdthesisid=myPhdthesisId).all()