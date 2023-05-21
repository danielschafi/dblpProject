"""
Author: GroupName
created: May 2022
Notes: -
"""

from db import db

class WwwAuthorListModel(db.Model):

    __tablename__ = "wwwauthorlist"
    id = db.Column(db.Integer, primary_key=True)

    authorid = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("AuthorModel")

    wwwid = db.Column(db.Integer, db.ForeignKey("www.id"))
    www = db.relationship("WwwModel")


    def __init__(self, authorid, wwwid):
        self.authorid = authorid
        self.wwwid = wwwid

    def to_json(self):
        return {self.id: {
            "author": self.author.to_json(),
            "www": self.www.to_json()
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
    def getByWwwId(cls, myWwwID):
        return cls.query.filter_by(wwwid=myWwwID).all()