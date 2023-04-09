"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from db import db

class AuthorModel(db.Model):

    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    orcid = db.Column(db.String(255))
    name = db.Column(db.String(255))

    def __init__(self, _id, orcId, name):
        self._id = _id
        self.orcId = orcId
        self.name = name

    def to_json(self):
        return {self.id: {
            "orcId": self.orcid,
            "name": self.name
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
        #Gets Author with author.id = myId from db
        #None, if author not found
        return cls.query.filter_by(id=myId).first()
    
#TODO: 
    @classmethod
    def getByOrcid(cls, myOrcId):
        #returns all authors filterd by orcID
        return cls.query.filter_by(orcid=myOrcId).all()