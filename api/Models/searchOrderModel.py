"""
Author: Adrian Joost
created: Mai 2022
Notes: -
"""

from db import db
import datetime

class SearchOrder(db.Model):

    __tablename__ = "search_order"
    id = db.Column(db.Integer, primary_key=True)
    current_status = db.Column(db.Integer)
    has_finished = db.Column(db.Integer)
    keyword = db.String(255)
    start_node = db.String(255)
    email = db.String(255)
    creation_time = db.Column(db.Integer)

    def __init__(self, keyword, start_node, email):
        self.keyword = keyword
        self.start_node = start_node
        self.email = email
        self.creation_time = datetime.now().timestamp()

    def to_json(self):
        return {self.id: {
            "current_status": self.current_status,
            "has_finished": self.has_finished,
            "keyword": self.keyword,
            "start_node": self.start_node,
            "email": self.email,
            "creation_time": self.creation_time
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
    def getByKeyword(cls, myKeyword):
        return cls.query.filter_by(keyword=myKeyword).all()