"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from db import db

class PublisherModel(db.Model):

    __tablename__ = "publisher"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def to_json(self):
        return {self.id: {
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
        #None if id not found
        return cls.query.filter_by(id=myId).first()
    
    @classmethod
    def getByName(cls, myName):
        return cls.query.filter_by(name=myName).all()