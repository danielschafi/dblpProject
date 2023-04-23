"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class IncollectionEeListModel(db.Model):

    __tablename__ = "incollectioneelist"
    id = db.Column(db.Integer, primary_key=True)

    eeid = db.Column(db.Integer, db.ForeignKey("ee.id"))
    ee = db.relationship("EeModel")

    incollectionid = db.Column(db.Integer, db.ForeignKey("incollection.id"))
    incollection = db.relationship("IncollectionModel")


    def __init__(self, eeid, incollectionid):
        self.eeid = eeid
        self.incollectionid = incollectionid

    def to_json(self):
        return {self.id: {
            "ee": self.ee.to_json(),
            "incollection": self.incollection.to_json()
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
    def getByIncollectionId(cls, myIncollID):
        return cls.query.filter_by(incollectionid=myIncollID).all()