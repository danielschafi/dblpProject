"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from db import db
from sqlalchemy import or_
from Models.proceedingsEditorListModel import ProceedingsEditorListModel
from Models.proceedingsEeListModel import ProceedingsEeListModel

class ProceedingsModel(db.Model):

    __tablename__ = "proceedings"
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(255))
    url = db.Column(db.String(255))
    isbn = db.Column(db.String(255))
    booktitle = db.Column(db.String(255))
    key = db.Column(db.String(255))
    title = db.Column(db.String(255))
    volume = db.Column(db.String(255))
    publisherid = db.Column(db.Integer(), db.ForeignKey("publisher.id"))
    publisher = db.relationship("PublisherModel")
    seriesid = db.Column(db.Integer(), db.ForeignKey("series.id"))
    series = db.relationship("SeriesModel")

    def __init__(self, year, url, isbn, booktitle, key, title, volume, publisherid, seriesid):
        self.year = year
        self.url = url
        self.isbn = isbn
        self.booktitle = booktitle
        self.title = title
        self.volume = volume
        self.key = key
        self.publisherid = publisherid
        self.seriesid = seriesid


    def to_json(self):
        return {self.id: {
            "year": self.year,
            "url": self.url,
            "isbn": self.isbn,
            "booktitle" : self.booktitle,
            "title" : self.title,
            "volume" : self.volume,
            "key" : self.key,
            "publisher": self.publisher.to_json(),
            "series": self.series.to_json()
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
    
    @classmethod
    def getByPublisherId(cls, myPublisherId):
        return cls.query.filter_by(publisherid=myPublisherId).all()
    
    @classmethod
    def getBySeries(cls, mySeries):
        return cls.query.filter_by(series=mySeries).all()

    @classmethod
    def getNodesKeyword(cls, keyword):
        results = cls.query.filter(or_(cls.title.contains(keyword), cls.booktitle.contains(keyword))).all()
        ids = []
        publishers = []
        series = []
        editors = []
        ees = []
        for result in results:
            ids.append(result.id)
            publishers.append(result.publisherid)
            series.append(result.seriesid)
            editorList = ProceedingsEditorListModel.getByProceedingsId(result.id)
            for link in editorList:
                editors.append(link.editorid)
            eeList = ProceedingsEeListModel.getByProceedingsId(result.id)
            for link in eeList:
                ees.append(link.eeid)
        publishers = set(publishers)
        series = set(series)
        editors = set(editors)
        ees = set(ees)
        return ids, series, publishers, editors, ees