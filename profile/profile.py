#from PurchaseActivity import amqp_setup
import bcrypt
import json
from os import environ
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify


# Add the parent directory to the system path


# setting path


# Create customer account /create/customer/<string:email> POST
# Create staff account /create/staff/<string:email> POST
# Create farmer account /create/farmer/<string:email> POST
# Get every ID in date  base /profile

# Updating customer account details /update/customer/<string:id> PUT
# Updating staff account details /update/staff/<string:id> PUT
# Updating farmer account details /update/farmer/<string:id> PUT
# Find customer details /profile/customer/<string:id> GET
# Find staff details /profile/staff/<string:id> GET
# Find farmer details /profile/farmer/<string:id> GET
# Password validation /profile/<string:email> GET

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'inventory_URL') or "mysql+mysqlconnector://root@localhost:3306/profile"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/profile'
# set dbURL=mysql+mysqlconnector://root@localhost:3306/profile
# docker run -p 5000:5003 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/profile mosengtim2021/profile:1.0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
salty = bcrypt.gensalt()


# Can change a bit


class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    profile_type = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(30))
    phone = db.Column(db.String(30))
    address = db.Column(db.String(30))

    def __init__(id, self, email, password, profile_type, name, phone, address):
        self.id = id
        self.email = email
        self.name = name
        self.phone = phone
        self.address = address
        self.password = bcrypt.hashpw(password.encode('utf-8'), salty)
        self.profile_type = profile_type

    def json(self):
        return {"id": self.id, "email": self.email,"phone":self.phone,"name":self.name,"address":self.address}

    def verify_password(self, passw):
        return (bcrypt.checkpw(passw.encode('utf-8'), self.password.encode('utf-8')))


# Creating customer account
@app.route("/create/<string:user_type>/<string:email>", methods=['POST'])
def create_account(email, user_type):
    # Find the profile with the matching particulars

    user_profiles = Profile.query.filter(
        db.and_(Profile.email == email, Profile.profile_type == user_type))
    user_profile = user_profiles.first()
    if (user_profile):
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
    print(data)
    profile = Profile(**data)
    print(profile.json())

    # Create another subtype
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
            "data": profile.json(),
            "userId": profile.id
        }
    ), 201


@app.route("/signIn/<string:user_type>", methods=['POST'])
def signIn(user_type):
    data = request.get_json()

    # If there is such an user with such then we will go and check the password
    user_profile = Profile.query.filter(db.and_(
        Profile.email == data['email'], Profile.profile_type == user_type)).first()
    if user_profile:
        if (user_profile.verify_password(data['password'])):
            return jsonify(

                {
                    "code": "200",
                    "userId": user_profile.id,
                    "message": "User provided Valid Login details"
                }
            )
        else:
            return jsonify(
                {
                    "code": "401",
                    "message": "User provided Invalid Login Details"
                }
            )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "User Provided Invalid Username"
            }
        ), 201


# Creating staff account


@ app.route("/create/farmer/<string:email>", methods=['POST'])
def create_farmer(email):
    if (Profile.query.filter_by(email=email).first()):
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
    profile = Farmer(email, **data)
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


# For getting the ID of every account
@ app.route("/profile")
def get_all_id():
    id_list = Profile.query.with_entities(Profile.id).all()
    if (len(id_list)):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "id": [id[0] for id in id_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no ids."
        }
    ), 404


# For adding customer details
@ app.route("/update/customer/<string:id>", methods=['PUT'])
def update_customer_profile(id):
    if (Customer.query.filter_by(id=id).first()):
        customer_details = Customer.query.filter_by(id=id).first()
        data = request.get_json()
        if (data['name'] != ''):
            customer_details.name = data['name']
        if (data['phone'] != ''):
            customer_details.phone = data['phone']
        if (data['address'] != ''):
            customer_details.address = data['address']
        try:
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
                "data": Customer.query.filter_by(id=id).first().json()
            }
        ), 201
    return jsonify(
        {
            "code": 400,
            "data": {
                "id": id
            },
            "message": "No such ID is used."
        }
    ), 400

# For adding staff details


@ app.route("/update/staff/<string:id>", methods=['PUT'])
def update_staff_profile(id):
    if (Staff.query.filter_by(id=id).first()):
        customer_details = Staff.query.filter_by(id=id).first()
        data = request.get_json()
        if (data['name'] != ''):
            customer_details.name = data['name']
        if (data['phone'] != ''):
            customer_details.phone = data['phone']
        if (data['address'] != ''):
            customer_details.address = data['address']
        try:
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
                "data": Staff.query.filter_by(id=id).first().json()
            }
        ), 201
    return jsonify(
        {
            "code": 400,
            "data": {
                "id": id
            },
            "message": "No such ID is used."
        }
    ), 400

# For adding farmer details


@ app.route("/update/farmer/<string:id>", methods=['PUT'])
def update_farmer_profile(id):
    if (Farmer.query.filter_by(id=id).first()):
        customer_details = Farmer.query.filter_by(id=id).first()
        data = request.get_json()
        if (data['name'] != ''):
            customer_details.name = data['name']
        if (data['phone'] != ''):
            customer_details.phone = data['phone']
        if (data['address'] != ''):
            customer_details.address = data['address']
        try:
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
                "data": Farmer.query.filter_by(id=id).first().json()
            }
        ), 201
    return jsonify(
        {
            "code": 400,
            "data": {
                "id": id
            },
            "message": "No such ID is used."
        }
    ), 400


# Find  profile
@ app.route("/profile/<string:id>")
# Get the profile corresponding to the profile
def find_profile(id):
    profile = Profile.query.filter_by(id=id).first()
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

# Find farmer profile


# Check for password
@ app.route("/profile/<string:email>", methods=['GET'])
def check_password(email):
    profile = Profile.query.filter_by(email=email).first()
    data = request.get_json()
    if (profile.verify_password(data['password'])):
        return jsonify(
            {
                "code": 200,
                "message": "Access granted"
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Password or username is incorrect."
        }
    ), 404


if __name__ == '__main__':
    print(__package__)
    app.run(host='0.0.0.0', port=5003, debug=True)


# class Customer(Profile):
# __tablename__ = 'customer'
# id = db.Column(db.Integer, db.ForeignKey('profile.id'), primary_key=True)
# name = db.Column(db.String(30))
# phone = db.Column(db.Integer)
# address = db.Column(db.String(30))

# def __init__(self, email, password):
#     super(Customer, self).__init__(email, password)

# def json(self):
#     return {"ID": self.id, "Name": self.name, "Phone": self.phone, "Address": self.address}

# class Staff(Profile):
#     __tablename__ = 'staff'
#     id = db.Column(db.Integer, db.ForeignKey('profile.id'), primary_key=True)
#     name = db.Column(db.String(30))
#     phone = db.Column(db.Integer)

#     def __init__(self, email, password):
#         super(Staff, self).__init__(email, password)

#     def json(self):
#         return {"ID": self.id, "Name": self.name, "Phone": self.phone}

# class Farmer(Profile):
#     __tablename__ = 'farmer'
#     id = db.Column(db.Integer, db.ForeignKey('profile.id'), primary_key=True)
#     name = db.Column(db.String(30))
#     phone = db.Column(db.Integer)
#     address = db.Column(db.String(30))

#     def __init__(self, email, password):
#         super(Farmer, self).__init__(email, password)

#     def json(self):
#         return {"ID": self.id, "Name": self.name, "Phone": self.phone, "Address": self.address}
