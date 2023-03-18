from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import json
import bcrypt

#Work done so far:
#Enable user to search for information about user
#Enable creation of user profiles
#Enable deletion of user profiles

app = Flask(__name__)
CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/profile'
# dbURL = 'mysql+mysqlconnector://root@localhost:3306/profile'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
salty = bcrypt.gensalt()

class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'),salty)


class Customer(Profile):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, db.ForeignKey('profile.id'), primary_key=True)
    name = db.Column(db.String(30))
    phone = db.Column(db.Integer)
    address = db.Column(db.String(30))

    def __init__(self, email, password):
        super(Customer, self).__init__(email, password)

    def json(self):
        return {"ID": self.id}
    
class Staff(Profile):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, db.ForeignKey('profile.id'), primary_key=True)
    name = db.Column(db.String(30))
    phone = db.Column(db.Integer)
    
    def __init__(self, email, password):
        super(Customer, self).__init__(email, password)

    def json(self):
        return {"ID": self.id}

class Farmer(Profile):
    __tablename__ = 'farmer'
    id = db.Column(db.Integer, db.ForeignKey('profile.id'), primary_key=True)
    name = db.Column(db.String(30))
    phone = db.Column(db.Integer)
    address = db.Column(db.String(30))
    
    def __init__(self, email, password):
        super(Farmer, self).__init__(email, password)

    def json(self):
        return {"ID": self.id}

#Creating customer account
@app.route("/create/customer/<string:email>", methods=['POST'])
def create_customer(email):
    if(Customer.query.filter_by(email=email).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "email": email
                },
                "message": "Email already taken."
            }
        ), 400
    data = request.get_json()
    profile = Customer(email, **data)
    try:
        db.session.add(profile)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": email
                },
                "message": "An error occurred creating the profile."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": profile.json()
        }
    ), 201

#For getting the ID of every account
@app.route("/profile")
def get_all_id():
    id_list = Profile.query.all()
    if(len(id_list)):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "id": [id.json() for id in id_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no ids."
        }
    ), 404

#For creating email, password
@app.route("/profile/create/<string:email>")
def create_profile(email):
    if(Profile.query.filter_by(email=email).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "Email already taken."
            }
        ), 400
    data = request.get_json()
    profile = Customer(id, **data)
    try:
        db.session.add(profile)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred creating the profile."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": profile.json()
        }
    ), 201









#Find customer profile
#Why can't this work 
# @app.route("/profile/<string:type>/<string:id>")
# def find_customer_profile(type, id):
#     type = type.capitalize()
#     print(type)
#     profile = type.query.filter_by(id=id).first()

@app.route("/profile/customer/<string:id>")
def find_customer_profile(id):
    profile = Customer.query.filter_by(id=id).first()
    if profile:
        return jsonify(
            {
            "code": 200,
            "data": profile.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Customer not found."
        }
    ), 404

#Find farmer profile
@app.route("/profile/farmer/<string:id>")
def find_farmer_profile(id):
    profile = Farmer.query.filter_by(id=id).first()
    if profile:
        return jsonify(
            {
            "code": 200,
            "data": profile.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Customer not found."
        }
    ), 404

#Find staff profile
@app.route("/profile/staff/<string:id>")
def find__profile(id):
    profile = Staff.query.filter_by(id=id).first()
    if profile:
        return jsonify(
            {
            "code": 200,
            "data": profile.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Customer not found."
        }
    ), 404










#Input customer details
@app.route("/profile/customer/<string:id>", methods=['POST'])
def create_customer_profile(id):
    if(Customer.query.filter_by(id=id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "Customer already exists."
            }
        ), 400
    data = request.get_json()
    profile = Customer(id, **data)
    try:
        db.session.add(profile)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred creating the profile."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": profile.json()
        }
    ), 201

#Create staff user profile 
@app.route("/profile/staff/<string:id>", methods=['POST'])
def create_staff_profile(id):
    if(Staff.query.filter_by(id=id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "Staff already exists."
            }
        ), 400
    data = request.get_json()
    profile = Staff(id, **data)
    try:
        db.session.add(profile)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred creating the profile."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": profile.json()
        }
    ), 201

#Create farmer user profile 
@app.route("/profile/farmer/<string:id>", methods=['POST'])
def create_farmer_profile(id):
    if(Farmer.query.filter_by(id=id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "Farmer already exists."
            }
        ), 400
    data = request.get_json()
    profile = Farmer(id, **data)
    try:
        db.session.add(profile)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred creating the profile."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": profile.json()
        }
    ), 201

#Check for password
@app.route("/profile/<string:email>", methods=['GET'])
def check_password(email):
    profile = Profile.query.filter_by(email=email).first()
    if profile:
        data = request.get_json()
        profile = Profile(id, **data)
        return jsonify(
            {
            "code": 200,
            "data": profile.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Password or username is incorrect."
        }
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
    print("Hello World")