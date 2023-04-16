"""
Author : GroupName
created: April 2022
Notes: -
"""

from db import db

class ProceedingsEditorListModel(db.Model):

    __tablename__ = "proceedingseditorlist"
    id = db.Column(db.Integer, primary_key=True)
    
    editorid = db.Column(db.Integer, db.ForeignKey("editor.id"))
    editor = db.relationship("EditorModel")

    proceedingsid = db.Column(db.Integer, db.ForeignKey("proceedings.id"))
    proceedings = db.relationship("ProceedingsModel")


    def __init__(self, _id, editorid, proceedingsid):
        self.id = _id
        self.editorid = editorid
        self.proceedingsid = proceedingsid

    def to_json(self):
        return {self.id: {
            "editor": self.editor.to_json(),
            "proceedings": self.proceedings.to_json()
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
    def getByProceedingsId(cls, myProceId):
        return cls.query.filter_by(proceedingsid=myProceId).all()