from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/person'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    
    def __init__(self, id):
        self.id = id
    
    def json(self):
        return {"isbn13": self.id}

class Customer(Person):
    __tablename__ = 'customer'
    name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(15), nullable=True)

    def __init__(self, id, name, email, phone, address):
        Person.__init__(id)
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def json(self):
        return {"isbn13": self.id ,"Name": self.name, "Email": self.email, "Phone": self.phone, "Address": self.address}
    
    def make_purchase_request(){
            
    }

class Staff(Person):
    __tablename__ = 'staff'
    name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.Integer, primary_key=True)

    def __init__(self, id, name, email, phone):
        Person.__init__(id)
        self.name = name
        self.email = email
        self.phone = phone

    def json(self):
        return {"isbn13": self.id ,"Name": self.name, "Email": self.email, "Phone": self.phone}



class Farmer(Person):
    __tablename__ = 'farmer'
    name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(15), nullable=True)

    def __init__(self, id, name, email, phone, address):
        Person.__init__(id)
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def json(self):
        return {"isbn13": self.id ,"Name": self.name, "Email": self.email, "Phone": self.phone, "Address": self.address}



@app.route("/make_purchase_request", methods=[ "PUT"])
def make_purchase_request():




if __name__ == '__main__':
    app.run(port=5000, debug=True)
    print("Hello World")
