"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class BookAuthorListModel(db.Model):

    __tablename__ = "bookauthorlist"
    id = db.Column(db.Integer, primary_key=True)

    authorid = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("AuthorModel")

    bookid = db.Column(db.Integer, db.ForeignKey("book.id"))
    book = db.relationship("BookModel")


    def __init__(self, _id, authorid, bookid):
        self.id = _id
        self.authorid = authorid
        self.bookid = bookid

    def to_json(self):
        return {self.id: {
            "author": self.author.to_json(),
            "book": self.book.to_json()
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
    def getByAuthorId(cls, myAuthorId):
        return cls.query.filter_by(authorid=myAuthorId).all()
    
    @classmethod
    def getByBookId(cls, myBookId):
        return cls.query.filter_by(bookid=myBookId).all()