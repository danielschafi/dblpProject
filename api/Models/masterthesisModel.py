"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

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
        for result in results:
            ids.append(result.id)
            schools.append(result.schoolid)
        #remove double Ids
        schools = set(schools)
        return ids, schools