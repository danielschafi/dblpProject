"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class InproceedingsEeListModel(db.Model):

    __tablename__ = "inproceedingseelist"
    id = db.Column(db.Integer, primary_key=True)

    inproceedingsid = db.Column(db.Integer, db.ForeignKey('inproceedings.id'))
    inproceedings = db.relationship('InproceedingsModel')

    eeid = db.Column(db.Integer, db.ForeignKey('ee.id'))
    ee = db.relationship('EeModel')


    def __init__(self, _id, inproceedingsid, eeid):
        self.id = _id
        self.inproceedingsid = inproceedingsid
        self.eeid = eeid


    def to_json(self):
        return {self.id: {
            "inproceedings": self.inproceedings.to_json(),
            "ee": self.ee.to_json()
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
    def getByInproceedingsId(cls, myInproceedingsId):
        return cls.query.filter_by(inproceedingsid=myInproceedingsId).all()
    
    @classmethod
    def getByEeId(cls, myEeId):
        return cls.query.filter_by(eeid=myEeId).all()