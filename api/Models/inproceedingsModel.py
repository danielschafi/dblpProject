"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db
from sqlalchemy import or_
from Models.inproceedingsAuthorListModel import InproceedingsAuthorListModel
from Models.inproceedingsEeListModel import InproceedingsEeListModel

class InproceedingsModel(db.Model):

    __tablename__ = "inproceedings"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    year = db.Column(db.String(255))
    crossref = db.Column(db.String(255))
    booktitle = db.Column(db.String(255))
    url = db.Column(db.String(255))
    pages = db.Column(db.String(255))
    key = db.Column(db.String(255))


    def __init__(self, title, year, crossref, booktitle, url, pages, key):
        self.title = title
        self.year = year
        self.crossref = crossref
        self.booktitle = booktitle
        self.url = url
        self.pages = pages
        self.key = key 


    def to_json(self):
        return {self.id: {
            "title": self.title,
            "year": self.year,
            "crossref": self.crossref,
            "booktitle": self.booktitle,
            "url": self.url,
            "pages": self.pages,
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
        #Gets inproceedings with inproceedings.id = myId from db
        #None, if inproceedings not found
        return cls.query.filter_by(id=myId).first()
    
    @classmethod
    def getNodesKeyword(cls, keyword):
        results = cls.query.filter(or_(cls.title.contains(keyword), cls.booktitle.contains(keyword))).all()
        ids = []
        authors = []
        ees = []
        for result in results:
            ids.append(result.id)
            authorList = InproceedingsAuthorListModel.getByInproceedingsId(result.id)
            for link in authorList:
                authors.append(link.authorid)
            eeList = InproceedingsEeListModel.getByInproceedingsId(result.id)
            for link in eeList:
                ees.append(link.eeid)
        return ids, authors, ees