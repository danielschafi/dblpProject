"""
Author: GroupName
created: April 2022
Notes: -
"""

from db import db

class BookEditorListModel(db.Model):

    __tablename__ = "bookEditorList"
    id = db.Column(db.Integer, primary_key=True)

    editorid = db.Column(db.Integer(), db.ForeignKey("editor.id"))
    editor = db.relationship("EditorModel")

    bookid = db.Column(db.Integer(), db.ForeignKey("book.id"))
    book = db.relationship("BookModel")


    def __init__(self, _id, editorid, bookid):
        self._id = _id
        self.editorid = editorid
        self.bookid = bookid

    def to_json(self):
        return {self.id: {
            "editor": self.editor.to_json(),
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
    def getByEditorId(cls, myEditorId):
        return cls.query.filter_by(editorid=myEditorId).all()
    
    @classmethod
    def getByBookId(cls, myBookId):
        return cls.query.filter_by(bookid=myBookId).all()