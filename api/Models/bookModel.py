"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class BookModel(db.Model):

    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    crossref = db.Column(db.String(255))
    title = db.Column(db.String(255))
    note = db.Column(db.String(255))
    volume = db.Column(db.String(255))
    pages = db.Column(db.String(255))
    year = db.Column(db.String(255))
    isbn = db.Column(db.String(255))
    key = db.Column(db.String(255))
    
    schoolid = db.Column(db.Integer, db.ForeignKey('school.id'))
    school = db.relationship('SchoolModel')
    seriesid = db.Column(db.Integer, db.ForeignKey('series.id'))
    series = db.relationship('SeriesModel')
    publisherid = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    publisher = db.relationship('PublisherModel')


    def __init__(self, crossref, title, note, volume, pages, year, isbn, key, schoolid, seriesid, publisherid):
        self.crossref = crossref
        self.title = title
        self.note = note
        self.volume = volume
        self.pages = pages
        self.year = year
        self.key = key
        self.isbn = isbn
        self.schoolid = schoolid
        self.seriesid = seriesid
        self.publisherid = publisherid


    def to_json(self):
        return {self.id: {
            "crossref": self.crossref,
            "title": self.title,
            "note": self.note,
            "volume": self.volume,
            "pages": self.pages,
            "year": self.year,
            "isbn": self.isbn,
            "key" : self.key,
            "school": self.school.to_json(),
            "series": self.series.to_json(),
            "publisher": self.publisher.to_json()
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
    
    @classmethod
    def getBySchoolId(cls, mySchoolId):
        return cls.query.filter_by(schoolid=mySchoolId).all()
    
    @classmethod
    def getBySeriesId(cls, mySeriesId):
        return cls.query.filter_by(seriesid=mySeriesId).all()
    
    @classmethod
    def getByPublisherId(cls, myPublisherId):
        return cls.query.filter_by(publisherid=myPublisherId).all()