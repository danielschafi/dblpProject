"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class WwwCiteListModel(db.Model):

    __tablename__ = "wwwcitelist"
    id = db.Column(db.Integer, primary_key=True)

    citeid = db.Column(db.Integer, db.ForeignKey("cite.id"))
    cite = db.relationship("CiteModel")

    wwwid = db.Column(db.Integer, db.ForeignKey("www.id"))
    www = db.relationship("WwwModel")


    def __init__(self, citeid, wwwid):
        self.citeid = citeid
        self.wwwid = wwwid

    def to_json(self):
        return {self.id: {
            "cite": self.cite.to_json(),
            "www": self.www.to_json()
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
        return cls.query.filter_by(citeid=myCiteId).all()
    
    @classmethod
    def getByWwwId(cls, myWwwId):
        return cls.query.filter_by(wwwid=myWwwId).all()