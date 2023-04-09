"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from db import db

class CiteModel(db.Model):

    __tablename__ = "cite"
    id = db.Column(db.Integer, primary_key=True)
    ref = db.Column(db.String(255))

    def __init__(self, _id, ref):
        self._id = _id
        self.ref = ref

    def to_json(self):
        return {self.id: {
            "ref": self.ref
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
    
    @classmethod
    def getByRef(cls, myRef):
        #returns all authors filterd by orcID
        return cls.query.filter_by(ref=myRef).all()