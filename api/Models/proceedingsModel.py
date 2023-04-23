"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from db import db

class ProceedingsModel(db.Model):

    __tablename__ = "proceedings"
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(255))
    url = db.Column(db.String(255))
    isbn = db.Column(db.String(255))
    publisherid = db.Column(db.Integer(), db.ForeignKey("publisher.id"))
    publisher = db.relationship("PublisherModel")

    def __init__(self, year, url, isbn, publisherid):
        self.year = year
        self.url = url
        self.isbn = isbn
        self.publisherid = publisherid

    def to_json(self):
        return {self.id: {
            "year": self.year,
            "url": self.url,
            "isbn": self.isbn,
            "publisher": self.publisher.to_json()
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
    def getByRef(cls, myRef):
        return cls.query.filter_by(ref=myRef).all()