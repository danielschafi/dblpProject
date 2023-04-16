"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class DataModel(db.Model):

    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    crossref = db.Column(db.String(255))
    title = db.Column(db.String(255))
    note = db.Column(db.String(255))
    number = db.Column(db.String(255))
    month = db.Column(db.String(255))
    year = db.Column(db.String(255))


    def __init__(self, _id, crossref, title, note, number, month, year):
        self._id = _id
        self.crossref = crossref
        self.title = title
        self.note = note
        self.number = number
        self.month = month
        self.year = year

    def to_json(self):
        return {self.id: {
            "crossref": self.crossref,
            "title": self.title,
            "note": self.note,
            "number": self.number,
            "month": self.month,
            "year": self.year
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
        #Gets dat with data.id = myId from db
        #None, if data not found
        return cls.query.filter_by(id=myId).first()
