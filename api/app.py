"""
Author: Adrian Joost
created: July 2022
Notes:
Entry point for API, this app will create a
link to the postgres db. It is important, that
posgres db runs on port 5432, user is 'postgres'
and password is 1234. Maybe, password should be imporved
when deploying API on production server
"""

from flask import Flask, render_template
from flask_restful import Api
from db import db
from Resources.authorRes import AuthorRes
from Resources.citeRes import CiteRes
from Resources.eeRes import EeRes
from Resources.eeTypeRes import EeTypeRes
from Resources.schoolRes import SchoolRes
from Resources.seriesRes import SeriesRes
from Resources.publisherRes import PublisherRes
from Resources.journalRes import JournalRes
from Resources.editorRes import EditorRes
from Resources.dataRes import DataRes
from Resources.proceedingsRes import ProceedingsRes
from Resources.proceedingsEeListRes import ProceedingsEeListRes as PLR
from Resources.articleAuthorListRes import ArticleAuthorListRes as AALR
from Resources.articleRes import ArticleRes
from Resources.articleEeListRes import ArticleEeListRes as AELR
from Resources.bookRes import BookRes
from Resources.bookAuthorListRes import BookAuthorListRes as BALR
from Resources.bookEditorListRes import BookEditorListRes as BELR
from Resources.bookEeListRes import BookEeListRes as BEELR
from Resources.dataAuthorListRes import DataAuthorListRes as DALR
from Resources.dataEeListRes import DataEeListRes as DELR
from Resources.incollectionRes import IncollectionRes
from Resources.incollectionAuthorListRes import IncollectionAuthorListRes as IALR
from Resources.incollectionCiteListRes import IncollectionCiteListRes as ICLR
from Resources.incollectionEeListRes import IncollectionEeListRes as IELR
from Resources.inproceedingsRes import InproceedingsRes
from Resources.inproceedingsAuthorListRes import InproceedingsAuthorListRes as INALR
from Resources.inproceedingsEeListRes import InproceedingsEeListRes as INELR
from Resources.masterthesisRes import MasterthesisRes
from Resources.masterthesisAuthorListRes import MasterthesisAuthorListRes as MALR
from Resources.MasterthesisEeListRes import MasterthesisEeListRes as MELM
from Resources.phdthesisRes import PhdthesisRes
from Resources.phdthesisAutorRes import PhdthesisAuthorListRes as PALR
from Resources.phdthesisEeListRes import PhdthesisEeListRes as PEELR
from Resources.proceedingsEditorListRes import ProceedingsEditorListRes as PELR
from Resources.wwwRes import WwwRes
from Resources.wwwCiteListRes import WwwCiteListRes as WCLR
from Resources.wwwAuthorListRes import WwwAuthorListRes as WALR
from Resources.keywordsRes import KeywordRes
from Resources.relationshipRes import RelationshipRes
from Resources.searchOrderRes import SearchOrderRes


app = Flask(__name__)

#URI to connect to Postgres DB
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/dblp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Setup API
app.secret_key = "1234"
api = Api(app)


#Create Tables in db object and do some woodomagic
@app.before_first_request
def create_table():
    db.create_all()
    
    
#Get API interface | currently not implemented
@app.route('/API', methods=['GET'])
def home():
    return render_template("API.html")

#Add API resources
api.add_resource(AuthorRes, "/api/author/<int:_id>")
api.add_resource(CiteRes, "/api/cite/<int:_id>")
api.add_resource(EeRes, "/api/ee/<int:_id>")
api.add_resource(EeTypeRes, "/api/eetype/<int:_id>")
api.add_resource(SchoolRes, "/api/school/<int:_id>")
api.add_resource(SeriesRes, "/api/series/<int:_id>")
api.add_resource(PublisherRes, "/api/publisher/<int:_id>")
api.add_resource(JournalRes, "/api/journal/<int:_id>")
api.add_resource(DataRes, "/api/data/<int:_id>")
api.add_resource(EditorRes, "/api/editor/<int:_id>")
api.add_resource(DALR, "/api/dataauthorlist/<int:_id>")
api.add_resource(DELR, "/api/dataeelist/<int:_id>")

api.add_resource(ProceedingsRes, "/api/proceedings/<int:_id>")
api.add_resource(PLR, "/api/proceedingseelist/<int:_id>")
api.add_resource(PELR, "/api/proceedingseditorlist/<int:_id>")

api.add_resource(AALR, "/api/articleauthorlist/<int:_id>")
api.add_resource(ArticleRes, "/api/article/<int:_id>")
api.add_resource(AELR, "/api/articleeelist/<int:_id>")

api.add_resource(BookRes, "/api/book/<int:_id>")
api.add_resource(BALR, "/api/bookauthorlist/<int:_id>")
api.add_resource(BELR, "/api/bookeditorlist/<int:_id>")
api.add_resource(BEELR, "/api/bookeelist/<int:_id>")


api.add_resource(IncollectionRes, "/api/incollection/<int:_id>")
api.add_resource(IALR, "/api/incollectionauthorlist/<int:_id>")
api.add_resource(ICLR, "/api/incollectioncitelist/<int:_id>")
api.add_resource(IELR, "/api/incollectioneelist/<int:_id>")

api.add_resource(InproceedingsRes, "/api/inproceedings/<int:_id>")
api.add_resource(INALR, "/api/inproceedingsauthorlist/<int:_id>")
api.add_resource(INELR, "/api/inproceedingseelist/<int:_id>")

api.add_resource(MasterthesisRes, "/api/masterthesis/<int:_id>")
api.add_resource(MALR, "/api/masterthesisauthorlist/<int:_id>")
api.add_resource(MELM, "/api/masterthesiseelist/<int:_id>")

api.add_resource(PhdthesisRes, "/api/phdthesis/<int:_id>")
api.add_resource(PALR, "/api/phdthesisauthorlist/<int:_id>")
api.add_resource(PEELR, "/api/phdthesiseelist/<int:_id>")

api.add_resource(WwwRes, "/api/www/<int:_id>")
api.add_resource(WCLR, "/api/wwwcitelist/<int:_id>")
api.add_resource(WALR, "/api/wwwauthorlist/<int:_id>")

api.add_resource(KeywordRes, "/api/keyword/<string:keyword>")
api.add_resource(RelationshipRes, "/api/relationship")
api.add_resource(SearchOrderRes, "/api/searchorder/<int:_id>")




if __name__ == "__main__":

    #setup DB
    db.init_app(app)

    #start app
    app.run(port=5000, host="0.0.0.0", debug=True, threaded=True)
