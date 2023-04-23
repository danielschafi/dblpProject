"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class IncollectionModel(db.Model):

    __tablename__ = "incollection"
    id = db.Column(db.Integer, primary_key=True)
    crossref = db.Column(db.String(255))
    title = db.Column(db.String(255))
    pages = db.Column(db.String(255))
    booktitle = db.Column(db.String(255))
    url = db.Column(db.String(255))
    year = db.Column(db.String(255))


    def __init__(self, crossref, title, pages, booktitle, url, year):
        self.crossref = crossref
        self.title = title
        self.pages = pages
        self.booktitle = booktitle
        self.url = url
        self.year = year
        

    def to_json(self):
        return {self.id: {
            "crossref": self.crossref,
            "title": self.title,
            "pages": self.pages,
            "booktitle": self.booktitle,
            "url": self.url,
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
        #Gets incollection with incollection.id = myId from db
        #None, if incollection not found
        return cls.query.filter_by(id=myId).first()