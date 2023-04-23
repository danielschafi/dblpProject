"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class DataAuthorListModel(db.Model):

    __tablename__ = "dataauthorlist"
    id = db.Column(db.Integer, primary_key=True)

    authorid = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("AuthorModel")

    dataid = db.Column(db.Integer, db.ForeignKey("data.id"))
    data = db.relationship("DataModel")


    def __init__(self, authorid, dataid):
        self.authorid = authorid
        self.dataid = dataid

    def to_json(self):
        return {self.id: {
            "author": self.author.to_json(),
            "data": self.data.to_json()
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
    def getByAuthorId(cls, myAuthorId):
        return cls.query.filter_by(authorid=myAuthorId).all()
    
    @classmethod
    def getByDataId(cls, myProceId):
        return cls.query.filter_by(dataid=myProceId).all()
