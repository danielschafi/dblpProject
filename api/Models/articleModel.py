"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class ArticleModel(db.Model):

    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    number = db.Column(db.String(255))
    pages = db.Column(db.String(255))
    url = db.Column(db.String(255))
    year = db.Column(db.String(255))
    journalid = db.Column(db.Integer(), db.ForeignKey("journal.id"))
    journal = db.relationship("JournalModel")

    def __init__(self, _id, title, number, pages, url, year, journalId):
        self._id = _id
        self.title = title
        self.number = number
        self.pages = pages
        self.url = url
        self.year = year
        self.journalId = journalId


    def to_json(self):
        return {self.id: {
            "title": self.title,
            "number": self.number,
            "pages": self.pages,
            "url": self.url,
            "year": self.year,
            "journal": self.journal.to_json()
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