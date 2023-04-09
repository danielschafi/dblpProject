"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from db import db

class EeModel(db.Model):

    __tablename__ = "ee"
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(255))

    def __init__(self, _id, link):
        self._id = _id
        self.link = link

    def to_json(self):
        return {self.id: {
            "link": self.link
        }}
    
    def save(self):
        #PUTS instance into db
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        #DELETES Entry with given primary key of instance
        #of this object.
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def get(cls, myId):
        #Get always filters by primary_key
        return cls.query.filter_by(id=myId).first()
    
    @classmethod
    def getByLink(cls, myLink):
        return cls.query.filter_by(link=myLink).all()