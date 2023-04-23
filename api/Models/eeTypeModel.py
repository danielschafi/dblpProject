"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from db import db

class EeTypeModel(db.Model):

    __tablename__ = "eetype"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255))

    def __init__(self, type):
        self.type = type

    def to_json(self):
        return {self.id: {
            "type": self.type
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
    def getByType(cls, myType):
        return cls.query.filter_by(type=myType).all()