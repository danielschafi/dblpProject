"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db
from Models.masterthesisAuthorListModel import MasterthesisAuthorListModel
from Models.masterthesisEeListModel import MasterthesisEeListModel

class MasterthesisModel(db.Model):

    __tablename__ = "masterthesis"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    note = db.Column(db.String(255))
    year = db.Column(db.String(255))
    key = db.Column(db.String(255))

    schoolid = db.Column(db.Integer, db.ForeignKey('school.id'))
    school = db.relationship('SchoolModel')


    def __init__(self, title, note, year, key, schoolid):
        self.title = title
        self.note = note
        self.year = year
        self.key = key
        self.schoolid = schoolid


    def to_json(self):
        return {self.id: {
            "title": self.title,
            "note": self.note,
            "year": self.year,
            "key" : self.key,
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
        #None, if element not found
        return cls.query.filter_by(id=myId).first()
    
    @classmethod
    def getBySchoolId(cls, mySchoolId):
        return cls.query.filter_by(schoolid=mySchoolId).all()
    
    @classmethod
    def getNodesKeyword(cls, keyword):
        results = cls.query.filter(cls.title.contains(keyword)).all()
        ids = []
        schools = []
        authors = []
        ees = []
        for result in results:
            ids.append(result.id)
            schools.append(result.schoolid)
            authorList = MasterthesisAuthorListModel.getByMastersthesisId(result.id)
            for link in authorList:
                authors.append(link.authorid)
            eeList = MasterthesisEeListModel.getByMasterthesisId(result.id)
            for link in eeList:
                ees.append(link.eeid)
        #remove double Ids
        schools = set(schools)
        authors = set(authors)
        ees = set(ees)
        return ids, schools, authors, ees