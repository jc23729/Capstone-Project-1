import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from search import check_flights
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import redirect


# app = Flask(__name__, )
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))
app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
# from app import db
# db.create_all()
#  exit()
db = SQLAlchemy(app)

# Database
class User(db.Model):
    email = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    user = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(80),nullable=False)
    frm = db.Column(db.String(80),nullable=False)
    to = db.Column(db.String(80),nullable=False)
    def __repr__(self):
        return "<user: {}>".format(self.user)

# Routes
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    content = request.json
    user = User(user=content["user"],email=content["email"],password = content["password"],frm = content["from"],to = content["to"] )
    db.session.add(user)
    db.session.commit()
    check_flights(content["email"], content["from"], content["to"])
    return {"message": "success"}

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return jsonify({"msg":"ok"})

# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     content = request.json
#     check_flights(content)
#     return jsonify({"msg":"ok"})

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()