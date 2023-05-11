"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class PhdthesisModel(db.Model):

    __tablename__ = "phdthesis"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    isbn = db.Column(db.String(255))
    note = db.Column(db.String(255))
    number = db.Column(db.String(255))
    pages = db.Column(db.String(255))
    volume = db.Column(db.String(255))
    year = db.Column(db.String(255))
    month = db.Column(db.String(255))
    key = db.Column(db.String(255))

    seriesid = db.Column(db.Integer, db.ForeignKey('series.id'))
    series = db.relationship('SeriesModel')

    publisherid = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    publisher = db.relationship('PublisherModel')
    
    schoolid = db.Column(db.Integer, db.ForeignKey('school.id'))
    school = db.relationship('SchoolModel')


    def __init__(self, title, isbn, note, number, pages, volume, year, month, key,  publisherid, schoolid, seriesid):
        self.title = title
        self.isbn = isbn
        self.note = note
        self.number = number
        self.pages = pages
        self.volume = volume
        self.year = year
        self.month = month
        self.key = key
        self.publisherid = publisherid
        self.schoolid = schoolid
        self.seriesid = seriesid

    def to_json(self):
        return {self.id: {
            "title": self.title,
            "isbn": self.isbn,
            "note": self.note,
            "number": self.number,
            "pages": self.pages,
            "volume": self.volume,
            "year": self.year,
            "month": self.month,
            "key" : self.key,
            "publisher": self.publisher.to_json(),
            "school": self.school.to_json(),
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
        #Gets Author with author.id = myId from db
        #None, if author not found
        return cls.query.filter_by(id=myId).first()
    
    @classmethod
    def getBySchoolId(cls, mySchoolId):
        return cls.query.filter_by(schoolid=mySchoolId).all()
    
    @classmethod
    def getByPublisherId(cls, myPublisherId):
        return cls.query.filter_by(publisherid=myPublisherId).all()
    
    @classmethod
    def getBySeriesId(cls, mySeriesId):
        return cls.query.filter_by(seriesid=mySeriesId).all()
    
    @classmethod
    def getByKeyword(cls, keyword):
        results = cls.query.filter(cls.title.contains(keyword)).all()
        ids = []
        for result in results:
            ids.append(result.id)
        return ids
    
    @classmethod
    def getByDoubleKeyword(cls, keyword, keywordTwo):
        results = cls.query.filter(cls.title.contains(keyword), cls.title.contains(keywordTwo)).all()
        ids = []
        for result in results:
            ids.append(result.id)
        return ids