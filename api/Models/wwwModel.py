"""
Author: Sangeeths Chandrakumar
created: April 2022
Notes: -
"""

from db import db

class WwwModel(db.Model):

    __tablename__ = "www"
    id = db.Column(db.Integer, primary_key=True)
    crossref = db.Column(db.String(255))
    title = db.Column(db.String(255))
    note = db.Column(db.String(255))
    url = db.Column(db.String(255))

    def __init__(self, _id, crossref, title, note, url):
        self._id = _id
        self.crossref = crossref
        self.title = title
        self.note = note
        self.url = url


    def to_json(self):
        return {self.id: {
            "crossref": self.crossref,
            "title": self.title,
            "note": self.note,
            "url": self.url
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