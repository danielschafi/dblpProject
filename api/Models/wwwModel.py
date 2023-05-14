"""
Author: GroupName
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
    key = db.Column(db.String(255))

    def __init__(self, crossref, title, note, url, key):
        self.crossref = crossref
        self.title = title
        self.note = note
        self.url = url
        self.key = key


    def to_json(self):
        return {self.id: {
            "crossref": self.crossref,
            "title": self.title,
            "note": self.note,
            "url": self.url,
            "key" : self.key
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
    def getNodesKeyword(cls, keyword):
        results = cls.query.filter(cls.title.contains(keyword)).all()
        ids = []
        for result in results:
            ids.append(result.id)
        return ids