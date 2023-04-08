from flask import Flask, render_template
from flask_restful import Api


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "TODO"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "superKevin"
api = Api(app)

@app.before_first_request
def create_table():
    #db.create_all()
    pass
    
    

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/controls', methods=['GET'])
def controls():
    return render_template("controls.html")


#api.add_resource(Nerve_Center, "/nerveCenter")
#api.add_resource(Thread_resource, "/thread/<string:thread_name>")

if __name__ == "__main__":


    #setup DB
    #db.init_app(app)

    
    #start app
    app.run(port=5000, host="0.0.0.0", debug=True, threaded=True)