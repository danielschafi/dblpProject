"""
Author: Adrian Joost
created: April 2022
Notes: -
"""

from db import db

class ProceedingsEeListModel(db.Model):

    __tablename__ = "proceedingseelist"
    id = db.Column(db.Integer, primary_key=True)
    eeid = db.Column(db.Integer(), db.ForeignKey("ee.id"))
    ee = db.relationship("EeModel")

    proceedingsid = db.Column(db.Integer(), db.ForeignKey("proceedings.id"))
    proceedings = db.relationship("ProceedingsModel")


    def __init__(self, _id, eeid, proceedingsid):
        self._id = _id
        self.eeid = eeid
        self.proceedingsid = proceedingsid

    def to_json(self):
        return {self.id: {
            "ee": self.ee.to_json(),
            "proceedings": self.proceedings.to_json()
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
    def getByEeId(cls, myEeId):
        return cls.query.filter_by(eeid=myEeId).all()
    
    @classmethod
    def getByProceedingsId(cls, myProceId):
        return cls.query.filter_by(proceedingsid=myProceId).all()