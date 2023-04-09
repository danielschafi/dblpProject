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


if __name__ == "__main__":

    #setup DB
    db.init_app(app)

    #start app
    app.run(port=5000, host="0.0.0.0", debug=True, threaded=True)