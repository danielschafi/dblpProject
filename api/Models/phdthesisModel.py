"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class PhdthesisModel(db.Model):

    __tablename__ = "phdthesis"
    id = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.String(255))
    title = db.Column(db.String(255))
    isbn = db.Column(db.String(255))
    note = db.Column(db.String(255))
    number = db.Column(db.String(255))
    pages = db.Column(db.String(255))
    volume = db.Column(db.Integer)
    year = db.Column(db.String(255))
    month = db.Column(db.String(255))

    publisherid = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    publisher = db.relationship('PublisherModel')
    
    schoolid = db.Column(db.Integer, db.ForeignKey('school.id'))
    school = db.relationship('SchoolModel')


    def __init__(self, _id, series, title, isbn, note, number, pages, volume, year, month, publisherid, schoolid):
        self._id = _id
        self.series = series
        self.title = title
        self.isbn = isbn
        self.note = note
        self.number = number
        self.pages = pages
        self.volume = volume
        self.year = year
        self.month = month
        self.publisherid = publisherid
        self.schoolid = schoolid

    def to_json(self):
        return {self.id: {
            "series": self.series,
            "title": self.title,
            "isbn": self.isbn,
            "note": self.note,
            "number": self.number,
            "pages": self.pages,
            "volume": self.volume,
            "year": self.year,
            "month": self.month,
            "publisher": self.publisher.to_json(),
            "school": self.school.to_json()
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