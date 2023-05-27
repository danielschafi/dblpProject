"""
Author: Cool Group
created: May 2022
Notes: -
"""

from db import db
from sqlalchemy import PrimaryKeyConstraint

class ConnectModel(db.Model):

    NOT_QUEUED = -1,
    QUEUED = 0
    QUEUED_AND_PASSED = 1

    __tablename__ = "connect"
    id = db.Column(db.Integer, primary_key=True)
    tablename = db.Column(db.String(255), primary_key=True)
    precedent_node = db.Column(db.String(255))
    visited = db.Column(db.Integer)
    queued = db.Column(db.Integer)
    orderid = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Integer)

    __table_args__ = (
        PrimaryKeyConstraint('id', 'tablename', 'orderid'),
    )


    def __init__(self, id, tablename, orderid):
        self.id = id
        self.tablename = tablename
        self.orderid = orderid
        self.precedent_node = None
        self.visited = 0
        self.queued = ConnectModel.NOT_QUEUED
        self.distance = -1

    def to_json(self):
        return {self.orderid: {
            "id": self.id,
            "tablename": self.tablename,
            "precedent_node": self.precedent_node,
            "visited": self.visited,
            "queued": self.queued,
            "distance": self.distance
        }}
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def queue(self):
        self.queue = ConnectModel.QUEUED
        self.save()
    
    def queueAndPass(self):
        self.queue = ConnectModel.QUEUED_AND_PASSED
        self.save()

    def setVisited(self):
        self.visited = 1
        self.save()

    def setDistance(self, dist):
        self.distance = dist
        self.save()

    def setPrecedentNode(self, preNode):
        self.precedent_node = preNode
        self.save()
        
    @classmethod
    def get(cls, id, orderid, tablename):
        #Get always filters by primary_key
        #Gets Author with author.id = myId from db
        #None, if author not found
        return cls.query.filter_by(orderid=orderid, id=id, tablename=tablename).first()
    
    @classmethod
    def getByOrderId(cls, myOrderId):
        #returns all authors filterd by orcID
        return cls.query.filter_by(orderid=myOrderId).all()
    
    @classmethod
    def multiInsert(cls, connectList):
        for connect in connectList:
            db.session.add(connect)
        db.session.commit()