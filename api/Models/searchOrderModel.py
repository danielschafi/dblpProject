"""
Author: Adrian Joost
created: Mai 2022
Notes: -
"""

from db import db
from datetime import datetime

class SearchOrderModel(db.Model):

    STATUS_SETUP = 0
    STATUS_PROCESSING = 1
    STATUS_FINISHED = 2

    __tablename__ = "search_order"
    id = db.Column(db.Integer, primary_key=True)
    current_status = db.Column(db.Integer)
    has_finished = db.Column(db.Integer)
    keyword = db.Column(db.String(255))
    start_node = db.Column(db.String(255))
    email = db.Column(db.String(255))
    max_distance = db.Column(db.Integer)
    creation_time = db.Column(db.Integer)

    def __init__(self, keyword, start_node, email, max_distance):
        self.keyword = keyword
        self.start_node = start_node
        self.email = email
        self.max_distance = max_distance
        self.has_finished = 0
        self.current_status = SearchOrderModel.STATUS_SETUP
        self.creation_time = datetime.now().timestamp()

    def to_json(self):
        return {self.id: {
            "current_status": self.current_status,
            "has_finished": self.has_finished,
            "keyword": self.keyword,
            "start_node": self.start_node,
            "email": self.email,
            "creation_time": int(self.creation_time)
        }}
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def changeStatus(self, status):
        self.current_status = status
        self.save()
        
    @classmethod
    def get(cls, myId):
        #Get always filters by primary_key
        #None if id not found
        return cls.query.filter_by(id=myId).first()
    
    @classmethod
    def getByKeyword(cls, myKeyword):
        return cls.query.filter_by(keyword=myKeyword).all()
        
    @classmethod
    def getByStatus(cls, status):
        return cls.query.filter_by(current_status=status).all()