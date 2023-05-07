"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from db import db

class ProceedingsModel(db.Model):

    __tablename__ = "proceedings"
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(255))
    url = db.Column(db.String(255))
    isbn = db.Column(db.String(255))
    booktitle = db.Columen(db.String(255))
    key = db.Column(db.String(255))
    publisherid = db.Column(db.Integer(), db.ForeignKey("publisher.id"))
    publisher = db.relationship("PublisherModel")
    seriesid = db.Column(db.Integer(), db.ForeignKey("series.id"))
    series = db.relationship("SeriesModel")

    def __init__(self, year, url, isbn, booktitle, key, publisherid, seriesid):
        self.year = year
        self.url = url
        self.isbn = isbn
        self.booktitle = booktitle
        self.key = key
        self.publisherid = publisherid
        self.seriesid = seriesid


    def to_json(self):
        return {self.id: {
            "year": self.year,
            "url": self.url,
            "isbn": self.isbn,
            "booktitle" : self.booktitle,
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
    def getBySeries(cls, mySeries):
        return cls.query.filter_by(series=mySeries).all()