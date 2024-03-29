"""
Author: GroupName
created: April 2022
Notes: -
"""
from sqlalchemy import or_
from db import db
from Models.incollectionAuthorListModel import IncollectionAuthorListModel
from Models.incollectionCiteListModel import IncollectionCiteListModel
from Models.incollectionEeListModel import IncollectionEeListModel

class IncollectionModel(db.Model):

    __tablename__ = "incollection"
    id = db.Column(db.Integer, primary_key=True)
    crossref = db.Column(db.String(255))
    title = db.Column(db.String(255))
    pages = db.Column(db.String(255))
    booktitle = db.Column(db.String(255))
    url = db.Column(db.String(255))
    year = db.Column(db.String(255))
    key = db.Column(db.String(255))


    def __init__(self, crossref, title, pages, booktitle, url, year, key):
        self.crossref = crossref
        self.title = title
        self.pages = pages
        self.booktitle = booktitle
        self.url = url
        self.year = year
        self.key = key
        

    def to_json(self):
        return {self.id: {
            "crossref": self.crossref,
            "title": self.title,
            "pages": self.pages,
            "booktitle": self.booktitle,
            "url": self.url,
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
        #Gets incollection with incollection.id = myId from db
        #None, if incollection not found
        return cls.query.filter_by(id=myId).first()
    
    @classmethod
    def getNodesKeyword(cls, keyword):
        results = cls.query.filter(or_(cls.title.contains(keyword), cls.booktitle.contains(keyword))).all()
        ids = []
        authors = []
        ees = []
        cites = []
        for result in results:
            ids.append(result.id)
            authorList = IncollectionAuthorListModel.getByIncollectionId(result.id)
            for link in authorList:
                authors.append(link.authorid)
            eeList = IncollectionEeListModel.getByIncollectionId(result.id)
            for link in eeList:
                ees.append(link.eeid)
            citeList = IncollectionCiteListModel.getByIncollectionId(result.id)
            for link in citeList:
                cites.append(link.citeid)
        authors = set(authors)
        ees = set(ees)
        cites = set(cites)        
        return ids, authors, ees, cites