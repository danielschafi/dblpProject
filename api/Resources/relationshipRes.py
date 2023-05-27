"""
Author: GroupName
created: April 2022
Notes: -
"""

from flask_restful import Resource, reqparse
from pseudocode import create_response, getDelParser

import importlib
Models = importlib.import_module("Models")
import os



class RelationshipRes(Resource):

    #Tuple of all tables in DB
    TABLE_NAMES = (
    "author", "cite", "editor",
    "journal", "school", "publisher",
    "series", "proceedings", "inproceedings",
    "data", "masterthesis", "phdthesis",
    "incollection", "book", "www", "article",
    "ee"
    )


    def get(self):
        
        parser = getGetParser()
        data = parser.parse_args()
        table = data["table"]
        relations = None
        if table == self.TABLE_NAMES[0]:
            relations = RelationshipRes.getAuthorRel(data["id"])
        elif table == self.TABLE_NAMES[1]:
            relations = RelationshipRes.getCiteRel(data["id"])
        elif table == self.TABLE_NAMES[2]:
            relations = RelationshipRes.getEditorRel(data["id"])
        elif table == self.TABLE_NAMES[3]:
            relations = RelationshipRes.getJournalRel(data["id"])
        elif table == self.TABLE_NAMES[4]:
            relations = RelationshipRes.getSchoolRel(data["id"])
        elif table == self.TABLE_NAMES[5]:
            relations = RelationshipRes.getPublisherRel(data["id"])
        elif table == self.TABLE_NAMES[6]:
            relations = RelationshipRes.getSeriesRel(data["id"])
        elif table == self.TABLE_NAMES[7]:
            relations = RelationshipRes.getProceedingsRel(data["id"])
        elif table == self.TABLE_NAMES[8]:
            relations = RelationshipRes.getInproceedingsRel(data["id"])
        elif table == self.TABLE_NAMES[9]:
            relations = RelationshipRes.getDataRel(data["id"])
        elif table == self.TABLE_NAMES[10]:
            relations = RelationshipRes.getMasterthesisRel(data["id"])
        elif table == self.TABLE_NAMES[11]:
            relations = RelationshipRes.getPhdthesisRel(data["id"])
        elif table == self.TABLE_NAMES[12]:
            relations = RelationshipRes.getIncollectionRel(data["id"])
        elif table == self.TABLE_NAMES[13]:
            relations = RelationshipRes.getBookRel(data["id"])
        elif table == self.TABLE_NAMES[14]:
            relations = RelationshipRes.getWwwRel(data["id"])
        elif table == self.TABLE_NAMES[15]:
            relations = RelationshipRes.getArticleRel(data["id"])
        elif table == self.TABLE_NAMES[16]:
            relations = RelationshipRes.getEeRel(data["id"])
        else:
            return create_response({"message":f"Table {data['table']} does not exist"}, 400)
        if relations:
            return create_response(relations, 200)
        return create_response({"message": f"The Node with table: {data['table']}"\
                                f" and id: {data['id']} does not exist"}, 404)
    
    @classmethod
    def getRelations(cls, table, _id):
        #yeah, its copied... Maybe change that as soon as a new table is added. :/
        relations = None
        if table == cls.TABLE_NAMES[0]:
            relations = RelationshipRes.getAuthorRel(_id)
        elif table == cls.TABLE_NAMES[1]:
            relations = RelationshipRes.getCiteRel(_id)
        elif table == cls.TABLE_NAMES[2]:
            relations = RelationshipRes.getEditorRel(_id)
        elif table == cls.TABLE_NAMES[3]:
            relations = RelationshipRes.getJournalRel(_id)
        elif table == cls.TABLE_NAMES[4]:
            relations = RelationshipRes.getSchoolRel(_id)
        elif table == cls.TABLE_NAMES[5]:
            relations = RelationshipRes.getPublisherRel(_id)
        elif table == cls.TABLE_NAMES[6]:
            relations = RelationshipRes.getSeriesRel(_id)
        elif table == cls.TABLE_NAMES[7]:
            relations = RelationshipRes.getProceedingsRel(_id)
        elif table == cls.TABLE_NAMES[8]:
            relations = RelationshipRes.getInproceedingsRel(_id)
        elif table == cls.TABLE_NAMES[9]:
            relations = RelationshipRes.getDataRel(_id)
        elif table == cls.TABLE_NAMES[10]:
            relations = RelationshipRes.getMasterthesisRel(_id)
        elif table == cls.TABLE_NAMES[11]:
            relations = RelationshipRes.getPhdthesisRel(_id)
        elif table == cls.TABLE_NAMES[12]:
            relations = RelationshipRes.getIncollectionRel(_id)
        elif table == cls.TABLE_NAMES[13]:
            relations = RelationshipRes.getBookRel(_id)
        elif table == cls.TABLE_NAMES[14]:
            relations = RelationshipRes.getWwwRel(_id)
        elif table == cls.TABLE_NAMES[15]:
            relations = RelationshipRes.getArticleRel(_id)
        elif table == cls.TABLE_NAMES[16]:
            relations = RelationshipRes.getEeRel(_id)
        return relations

        
    
    @classmethod
    def getAuthorRel(cls, _id):
        #returns all Ids of Nodes as dict connected to this table with id. If return = None, Node does not exist
        author = Models.authorModel.AuthorModel.get(_id)
        if not author:
            return None
        returnValue = {}
        #getArticles
        articles = Models.ArticleAuthorListModel.getByAuthorId(_id)
        articlesIds = []
        for article in articles:
            articlesIds.append(article.articleid)
        returnValue["article"] = articlesIds
        #get Books
        books = Models.bookAuthorListModel.BookAuthorListModel.getByAuthorId(_id)
        booksIds = []
        for book in books:
            booksIds.append(book.bookid)
        returnValue["book"] = booksIds
        #Get Data
        datas = Models.DataAuthorListModel.getByAuthorId(_id)
        dataIds = []
        for data in datas:
            dataIds.append(data.dataid)
        returnValue["data"] = dataIds
        #Get Incollection
        incollections = Models.IncollectionAuthorListModel.getByAuthorId(_id)
        incollectionIds = []
        for incol in incollections:
            incollectionIds.append(incol.incollectionid)
        returnValue["incollection"] = incollectionIds
        #Get Inproceedings
        inproceedings = Models.InproceedingsAuthorListModel.getByAuthorId(_id)
        inprocIds = []
        for inproc in inproceedings:
            inprocIds.append(inproc.inproceedingsid)
        returnValue["inproceedings"] = inprocIds
        #Get Masterthesis
        masterthesi = Models.MasterthesisAuthorListModel.getByAuthorId(_id)
        mastIds = []
        for masterthesis in masterthesi:
            mastIds.append(masterthesis.id)
        returnValue["masterthesis"] = mastIds
        #Get PHDThesis
        phds = Models.PhdthesisAuthorListModel.getByAuthorId(_id)
        phdIds = []
        for phd in phds:
            phdIds.append(phd.phdthesisid)
        returnValue["phdthesis"] = phdIds
        #Get www
        wwws = Models.WwwAuthorListModel.getByAuthorId(_id)
        wwwIds = []
        for www in wwws:
            wwwIds.append(www.wwwid)
        returnValue["www"] = wwwIds
        return returnValue

    @classmethod    
    def getCiteRel(cls, _id):
        #returns all Ids of Nodes as dict connected to this table with id. If return = None, Node does not exist
        cite = Models.citeModel.CiteModel.get(_id)
        if not cite:
            return None
        returnValue = {}
        #getIncollections
        incols = Models.IncollectionCiteListModel.getByCiteId(_id)
        incolsIds = []
        for incol in incols:
            incolsIds.append(incol.incollectionid)
        returnValue["Incollection"] = incolsIds
        #getWwws
        wwws = Models.WwwCiteListModel.getByCiteId(_id)
        wwwIds = []
        for a in wwws:
            wwwIds.append(a.wwwid)
        returnValue["www"] = wwwIds
        return returnValue

    @classmethod
    def getEditorRel(cls, _id):
        editor = Models.EditorModel.get(_id)
        if not editor:
            return None
        returnValue = {}
        #getBooks
        books = Models.BookEditorListModel.getByEditorId(_id)
        booksIds = []
        for book in books:
            booksIds.append(book.bookid)
        returnValue["book"] = booksIds
        #getProceedings | from here we ninja-code for simplicity...
        proceedings = Models.ProceedingsEditorListModel.getByEditorId(_id)
        a = []
        for n in proceedings:
            a.append(n.bookid)
        returnValue["proceeding"] = a
        

        return returnValue

    @classmethod
    def getJournalRel(cls, _id):
        journal = Models.JournalModel.get(_id)
        if not journal:
            return None
        returnValue = {}
        #getArticles
        nodes = Models.ArticleModel.getByJournalId(_id)
        ids = []
        for node in nodes:
            ids.append(node.id)
        returnValue["article"] = ids
        return returnValue

    @classmethod
    def getSchoolRel(cls, _id):
        school = Models.SchoolModel.get(_id)
        if not school:
            return None
        returnValue = {}
        #getBooks
        nodes = Models.BookModel.getBySchoolId(_id)
        ids = []
        for node in nodes:
            ids.append(node.id)
        returnValue["book"] = ids
        #getMasterthesis
        nodes = Models.MasterthesisModel.getBySchoolId(_id)
        ids = []
        for node in nodes:
            ids.append(node.id)
        returnValue["masterthesis"] = ids
        #getPHDThesis
        nodes = Models.PhdthesisModel.getBySchoolId(_id)
        ids = []
        for node in nodes:
            ids.append(node.id)
        returnValue["phdthesis"] = ids
        return returnValue

    @classmethod
    def getPublisherRel(cls, _id):
        publisher = Models.PublisherModel.get(_id)
        if not publisher:
            return None
        returnValue = {}
        #getBooks
        nodes = Models.BookModel.getByPublisherId(_id)
        ids = []
        for node in nodes:
            ids.append(node.id)
        returnValue["book"] = ids
        #getPhds
        nodes = Models.PhdthesisModel.getByPublisherId(_id)
        ids = []
        for node in nodes:
            ids.append(node.id)
        returnValue["phdthesis"] = ids
        #getProceedings
        nodes = Models.ProceedingsModel.getByPublisherId(_id)
        ids = []
        for node in nodes:
            ids.append(node.id)
        returnValue["proceeding"] = ids
        return returnValue
    
    @classmethod
    def getSeriesRel(cls, _id):
        series = Models.SeriesModel.get(_id)
        if not series:
            return None
        returnValue = {}
        #getBooks
        nodes = Models.BookModel.getBySeriesId(_id)
        ids = []
        for node in nodes:
            ids.append(node.id)
        returnValue["book"] = ids
        #getPhd
        nodes = Models.PhdthesisModel.getBySeriesId(_id)
        ids = []
        for node in nodes:
            ids.append(node.id)
        returnValue["phdthesis"] = ids
        return returnValue
    
    @classmethod
    def getProceedingsRel(cls, _id):
        proc = Models.ProceedingsModel.get(_id)
        if not proc:
            return None
        returnValue = {}
        #get Ee
        nodes = Models.ProceedingsEeListModel.getByProceedingsId(_id)
        ids = []
        for node in nodes:
            ids.append(node.eeid)
        returnValue["ee"] = ids
        #get Editor
        nodes = Models.ProceedingsEditorListModel.getByProceedingsId(_id)
        ids = []
        for node in nodes:
            ids.append(node.editorid)
        returnValue["editor"] = ids
        #add publisher
        returnValue["publisher"] = [proc.publisherid]
        #add series
        returnValue["series"] = [proc.seriesid]
        return returnValue
    
    @classmethod
    def getInproceedingsRel(cls, _id):
        inproc = Models.InproceedingsModel.get(_id)
        if not inproc:
            return None
        returnValue = {}
        #get autor
        nodes = Models.InproceedingsAuthorListModel.getByInproceedingsId(_id)
        ids = []
        for node in nodes:
            ids.append(node.authorid)
        returnValue["author"] = ids
        #get EEs
        nodes = Models.InproceedingsEeListModel.getByInproceedingsId(_id)
        ids = []
        for node in nodes:
            ids.append(node.eeid)
        returnValue["ee"] = ids
        return returnValue
    
    @classmethod
    def getDataRel(cls, _id):
        data = Models.DataModel.get(_id)
        if not data:
            return None
        returnValue = {}
        #get autohors
        nodes = Models.DataAuthorListModel.getByDataId(_id)
        ids = []
        for node in nodes:
            ids.append(node.authorid)
        returnValue["author"] = ids
        #get EEs
        nodes = Models.DataEeListModel.getByDataId(_id)
        ids = []
        for node in nodes:
            ids.append(node.eeid)
        returnValue["ee"] = ids
        
        return returnValue
    
    @classmethod
    def getMasterthesisRel(cls, _id):
        thesis = Models.MasterthesisModel.get(_id)
        if not thesis:
            return None
        returnValue = {}
        #getSchool
        returnValue["school"] = [thesis.schoolid]
        #get autohors
        nodes = Models.MasterthesisAuthorListModel.getByMastersthesisId(_id)
        ids = []
        for node in nodes:
            ids.append(node.authorid)
        returnValue["author"] = ids
        #get EEs
        nodes = Models.MasterthesisEeListModel.getByMasterthesisId(_id)
        ids = []
        for node in nodes:
            ids.append(node.eeid)
            returnValue["ee"] = ids
        return returnValue
    
    @classmethod
    def getPhdthesisRel(cls, _id):
        thesis = Models.PhdthesisModel.get(_id)
        if not thesis:
            return None
        returnValue = {}
        returnValue["school"] = [thesis.schoolid]
        returnValue["series"] = [thesis.seriesid]
        returnValue["publisher"] = [thesis.publisherid]
        #Get Authors
        nodes = Models.PhdthesisAuthorListModel.getByPhdthesisId(_id)
        ids = []
        for node in nodes:
            ids.append(node.authorid)
        returnValue["author"] = ids
        #get EE
        nodes = Models.PhdthesisEeListModel.getByPhdthesisId(_id)
        ids = []
        for node in nodes:
            ids.append(node.eeid)
            returnValue["ee"] = ids

        return returnValue
    
    @classmethod
    def getIncollectionRel(cls, _id):
        incol = Models.IncollectionModel.get(_id)
        if not incol:
            return None
        returnValue = {}
        #Get Authors
        nodes = Models.IncollectionAuthorListModel.getByIncollectionId(_id)
        ids = []
        for node in nodes:
            ids.append(node.authorid)
        returnValue["author"] = ids
        #get EE
        nodes = Models.IncollectionEeListModel.getByIncollectionId(_id)
        ids = []
        for node in nodes:
            ids.append(node.eeid)
        returnValue["ee"] = ids
        #Get Cites
        nodes = Models.IncollectionCiteListModel.getByIncollectionId(_id)
        ids = []
        for node in nodes:
            ids.append(node.citeid)
        returnValue["cite"] = ids
        return returnValue
    
    @classmethod
    def getBookRel(cls, _id):
        book = Models.BookModel.get(_id)
        if not book:
            return None
        returnValue = {}
        #add stuff
        returnValue["school"] = [book.schoolid]
        returnValue["series"] = [book.seriesid]
        returnValue["publisher"] = [book.publisherid]
        #Get Authors
        nodes = Models.BookAuthorListModel.getByBookId(_id)
        ids = []
        for node in nodes:
            ids.append(node.authorid)
        returnValue["author"] = ids
        #Get Editor
        nodes = Models.BookEditorListModel.getByBookId(_id)
        ids = []
        for node in nodes:
            ids.append(node.editorid)
        returnValue["editor"] = ids
        #Get Ee
        nodes = Models.BookEeListModel.getByBookId(_id)
        ids = []
        for node in nodes:
            ids.append(node.eeid)
        returnValue["ee"] = ids
        return returnValue

    @classmethod
    def getWwwRel(cls, _id):
        www = Models.WwwModel.get(_id)
        if not www:
            return None
        returnValue = {}
        #Get Authors
        nodes = Models.WwwAuthorListModel.getByWwwId(_id)
        ids = []
        for node in nodes:
            ids.append(node.authorid)
        returnValue["author"] = ids
        #Get Cite
        nodes = Models.WwwCiteListModel.getByWwwId(_id)
        ids = []
        for node in nodes:
            ids.append(node.citeid)
        returnValue["cite"] = ids
        return returnValue

    @classmethod
    def getArticleRel(cls, _id):
        article = Models.ArticleModel.get(_id)
        if not article:
            return None
        returnValue = {}
        returnValue["journal"] = [article.journalid]
        #Get Authors
        nodes = Models.ArticleAuthorListModel.getByArticleId(_id)
        ids = []
        for node in nodes:
            ids.append(node.authorid)
        returnValue["author"] = ids
        #Get Ee
        nodes = Models.ArticleEeListModel.getByArticleId(_id)
        ids = []
        for node in nodes:
            ids.append(node.eeid)
        returnValue["ee"] = ids
        return returnValue

    @classmethod
    def getEeRel(cls, _id):
        ee = Models.EeModel.get(_id)
        if not ee:
            return None
        returnValue = {}
        #Get article
        nodes = Models.ArticleEeListModel.getByEeId(_id)
        ids = []
        for node in nodes:
            ids.append(node.articleid)
        returnValue["article"] = ids
        #Get book
        nodes = Models.BookEeListModel.getByEeId(_id)
        ids = []
        for node in nodes:
            ids.append(node.bookid)
        returnValue["book"] = ids
        #Get Data
        nodes = Models.DataEeListModel.getByEeId(_id)
        ids = []
        for node in nodes:
            ids.append(node.dataid)
        returnValue["data"] = ids
        #Get incollection
        nodes = Models.IncollectionEeListModel.getByEeId(_id)
        ids = []
        for node in nodes:
            ids.append(node.incollectionid)
        returnValue["incollection"] = ids
        #Get inproceedings
        nodes = Models.InproceedingsEeListModel.getByEeId(_id)
        ids = []
        for node in nodes:
            ids.append(node.inproceedingsid)
        returnValue["inproceedings"] = ids
        #Get mastersthesis
        nodes = Models.MasterthesisEeListModel.getByEeId(_id)
        ids = []
        for node in nodes:
            ids.append(node.masterthesisid)
        returnValue["masterthesis"] = ids
        #Get phd
        nodes = Models.PhdthesisEeListModel.getByEeId(_id)
        ids = []
        for node in nodes:
            ids.append(node.phdthesisid)
        returnValue["phdthesis"] = ids
        #Get proceedings
        nodes = Models.ProceedingsEeListModel.getByEeId(_id)
        ids = []
        for node in nodes:
            ids.append(node.proceedingsid)
        returnValue["proceedings"] = ids

        return returnValue

        




def getGetParser():
    #returns a reqparser for the article post method
    parser = reqparse.RequestParser()
    parser.add_argument("id",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("table",
                        type=str,
                        required=True,
                        help="This field cannot be left blank")
    return parser