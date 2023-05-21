"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db
from Models.journalModel import JournalModel

class ArticleModel(db.Model):

    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    number = db.Column(db.String(255))
    pages = db.Column(db.String(255))
    url = db.Column(db.String(255))
    year = db.Column(db.String(255))
    volume = db.Column(db.String(255))
    key = db.Column(db.String(255))
    journalid = db.Column(db.Integer, db.ForeignKey("journal.id"))
    journal = db.relationship("JournalModel")

    def __init__(self, title, number, pages, url, year, volume,  key, journalid):
        #self._id = _id
        self.title = title
        self.number = number
        self.pages = pages
        self.url = url
        self.year = year
        self.volume = volume
        self.key = key
        self.journalid = journalid


    def to_json(self):
        return {self.id: {
            "title": self.title,
            "number": self.number,
            "pages": self.pages,
            "url": self.url,
            "year": self.year,
            "volume":self.volume,
            "key" : self.key,
            "journal": self.journal.to_json()
        }}
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def getJournal(self):
        self.journal = JournalModel.get(self.journalid)
        
    @classmethod
    def get(cls, myId):
        #Get always filters by primary_key
        #None if id not found
        return cls.query.filter_by(id=myId).first()
    
    @classmethod
    def getByJournalId(cls, myId):
        return cls.query.filter_by(journalid=myId).all()
    
    @classmethod
    def getByRef(cls, myRef):
        return cls.query.filter_by(ref=myRef).all()
    
    @classmethod
    def getNodesKeyword(cls, keyword):
        results = cls.query.filter(cls.title.contains(keyword)).all()
        ids = []
        journals = []
        for result in results:
            ids.append(result.id)
            journals.append(result.journalid)
        #remove double Ids
        journals = set(journals)
        return ids, journals