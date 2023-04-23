"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class IncollectionCiteListModel(db.Model):

    __tablename__ = "incollectioncitelist"
    id = db.Column(db.Integer, primary_key=True)

    citeid = db.Column(db.Integer, db.ForeignKey("cite.id"))
    cite = db.relationship("CiteModel")

    incollectionid = db.Column(db.Integer, db.ForeignKey("incollection.id"))
    incollection = db.relationship("IncollectionModel")


    def __init__(self, citeid, incollectionid):
        self.citeid = citeid
        self.incollectionid = incollectionid

    def to_json(self):
        return {self.id: {
            "cite": self.cite.to_json(),
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
    def getByCiteId(cls, myCiteId):
        return cls.query.filter_by(citeId=myCiteId).all()
    
    @classmethod
    def getByIncollectionId(cls, myIncollectionId):
        return cls.query.filter_by(incollectionid=myIncollectionId).all()