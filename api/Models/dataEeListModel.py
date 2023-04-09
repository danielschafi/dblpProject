"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class DataEeListModel(db.Model):

    __tablename__ = "dataeeList"
    id = db.Column(db.Integer, primary_key=True)

    eeid = db.Column(db.Integer(), db.ForeignKey("ee.id"))
    ee = db.relationship("EeModel")

    dataid = db.Column(db.Integer(), db.ForeignKey("data.id"))
    data = db.relationship("DataModel")


    def __init__(self, _id, eeid, dataid):
        self._id = _id
        self.eeid = eeid
        self.dataid = dataid

    def to_json(self):
        return {self.id: {
            "ee": self.ee.to_json(),
            "data": self.data.to_json()
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
    def getByEeId(cls, myEeId):
        return cls.query.filter_by(eeid=myEeId).all()
    
    @classmethod
    def getByDataId(cls, myProceId):
        return cls.query.filter_by(dataid=myProceId).all()
