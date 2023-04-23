"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class MasterthesisEeListModel(db.Model):

    __tablename__ = "masterthesiseelist"
    id = db.Column(db.Integer, primary_key=True)

    eeid = db.Column(db.Integer, db.ForeignKey("ee.id"))
    ee = db.relationship("EeModel")

    masterthesisid = db.Column(db.Integer, db.ForeignKey("masterthesis.id"))
    masterthesis = db.relationship("MasterthesisModel")


    def __init__(self, eeid, masterthesisid):
        self.eeid = eeid
        self.masterthesisid = masterthesisid

    def to_json(self):
        return {self.id: {
            "Ee": self.ee.to_json(),
            "masterthesis": self.masterthesis.to_json()
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
    def getByMasterthesisId(cls, myMasterthesisId):
        return cls.query.filter_by(masterthesisid=myMasterthesisId).all()