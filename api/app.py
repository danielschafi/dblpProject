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
from Resources.publisherRes import PublisherRes
from Resources.journalRes import JournalRes
from Resources.editorRes import EditorRes
from Resources.proceedingsRes import ProceedingsRes
from Resources.proceedingsEeListRes import ProceedingsEeListRes as PLR
from Resources.articleAuthorListRes import ArticleAuthorListRes as AALM
from Resources.articleRes import ArticleRes
from Resources.articleEeListRes import ArticleEeListRes as AELM
from Resources.bookRes import BookRes

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
api.add_resource(PublisherRes, "/api/publisher/<int:_id>")
api.add_resource(JournalRes, "/api/journal/<int:_id>")
api.add_resource(EditorRes, "/api/editor/<int:_id>")
api.add_resource(ProceedingsRes, "/api/proceedings/<int:_id>")
api.add_resource(PLR, "/api/proceedingseelist/<int:_id>")
api.add_resource(AALM, "/api/articleauthorlist/<int:_id>")
api.add_resource(ArticleRes, "/api/article/<int:_id>")
api.add_resource(AELM, "/api/articleeelist/<int:_id>")
api.add_resource(BookRes, "/api/book/<int:_id>")


if __name__ == "__main__":

    #setup DB
    db.init_app(app)

    #start app
    app.run(port=5000, host="0.0.0.0", debug=True, threaded=True)