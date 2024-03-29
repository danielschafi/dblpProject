"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db
from Models.dataAuthorListModel import DataAuthorListModel
from Models.dataEeListModel import DataEeListModel

class DataModel(db.Model):

    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    crossref = db.Column(db.String(255))
    title = db.Column(db.String(255))
    note = db.Column(db.String(255))
    number = db.Column(db.String(255))
    month = db.Column(db.String(255))
    year = db.Column(db.String(255))
    key = db.Column(db.String(255))


    def __init__(self, crossref, title, note, number, month, year, key):
        self.crossref = crossref
        self.title = title
        self.note = note
        self.number = number
        self.month = month
        self.year = year
        self.key = key

    def to_json(self):
        return {self.id: {
            "crossref": self.crossref,
            "title": self.title,
            "note": self.note,
            "number": self.number,
            "month": self.month,
            "year": self.year,
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
        #Gets dat with data.id = myId from db
        #None, if data not found
        return cls.query.filter_by(id=myId).first()
    
    @classmethod
    def getNodesKeyword(cls, keyword):
        results = cls.query.filter(cls.title.contains(keyword)).all()
        ids = []
        authors = []
        ees = []
        for result in results:
            ids.append(result.id)
            authorList = DataAuthorListModel.getByDataId(result.id)
            for link in authorList:
                authors.append(link.authorid)
            eeList = DataEeListModel.getByDataId(result.id)
            for link in eeList:
                ees.append(link.eeid)
        authors = set(authors)
        ees = set(ees)
        return ids, authors, ees
