"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class InproceedingsModel(db.Model):

    __tablename__ = "inproceedings"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    year = db.Column(db.String(255))
    crossref = db.Column(db.String(255))
    booktitle = db.Column(db.String(255))
    url = db.Column(db.String(255))
    pages = db.Column(db.String(255))


    def __init__(self, _id, title, year, crossref, booktitle, url, pages):
        self._id = _id
        self.title = title
        self.year = year
        self.crossref = crossref
        self.booktitle = booktitle
        self.url = url
        self.pages = pages


    def to_json(self):
        return {self.id: {
            "title": self.title,
            "year": self.year,
            "crossref": self.crossref,
            "booktitle": self.booktitle,
            "url": self.url,
            "pages": self.pages
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
