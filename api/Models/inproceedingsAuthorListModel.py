"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class InproceedingsAuthorListModel(db.Model):

    __tablename__ = "inproceedingsauthorlist"
    id = db.Column(db.Integer, primary_key=True)

    inproceedingsid = db.Column(db.Integer, db.ForeignKey('inproceedings.id'))
    inproceedings = db.relationship('InproceedingsModel')

    authorid = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('AuthorModel')


    def __init__(self, inproceedingsid, authorid):
        self.inproceedingsid = inproceedingsid
        self.authorid = authorid


    def to_json(self):
        return {self.id: {
            "inproceedings": self.inproceedings.to_json(),
            "author": self.author.to_json()
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
        #None, if element not found
        return cls.query.filter_by(id=myId).first()

    @classmethod
    def getByInproceedingsId(cls, myInproceedingsId):
        return cls.query.filter_by(inproceedingsid=myInproceedingsId).all()
    
    @classmethod
    def getByAuthorId(cls, myAuthorId):
        return cls.query.filter_by(authorid=myAuthorId).all()