"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class IncollectionAuthorListModel(db.Model):

    __tablename__ = "incollectionAuthorList"
    id = db.Column(db.Integer, primary_key=True)

    authorid = db.Column(db.Integer(), db.ForeignKey("author.id"))
    author = db.relationship("AuthorModel")

    incollectionid = db.Column(db.Integer(), db.ForeignKey("incollection.id"))
    incollection = db.relationship("IncollectionModel")


    def __init__(self, _id, authorid, incollectionid):
        self._id = _id
        self.authorid = authorid
        self.incollectionid = incollectionid

    def to_json(self):
        return {self.id: {
            "author": self.author.to_json(),
            "incollection": self.incollection.to_json()
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
        return cls.query.filter_by(eeid=myAuthorId).all()
    
    @classmethod
    def getByIncollectionId(cls, myIncollectionId):
        return cls.query.filter_by(incollectionid=myIncollectionId).all()