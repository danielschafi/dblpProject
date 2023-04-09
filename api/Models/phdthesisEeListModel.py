"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class PhdthesisEeListModel(db.Model):

    __tablename__ = "phdthesisEeList"
    id = db.Column(db.Integer, primary_key=True)

    eeid = db.Column(db.Integer(), db.ForeignKey("ee.id"))
    ee = db.relationship("EeModel")

    phdthesisid = db.Column(db.Integer(), db.ForeignKey("phdthesis.id"))
    phdthesis = db.relationship("PhdthesisModel")


    def __init__(self, _id, eeid, phdthesisid):
        self._id = _id
        self.eeid = eeid
        self.phdthesisid = phdthesisid

    def to_json(self):
        return {self.id: {
            "ee": self.ee.to_json(),
            "phdthesis": self.phdthesis.to_json()
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
    def getByPhdthesisId(cls, myProceId):
        return cls.query.filter_by(phdthesisid=myProceId).all()