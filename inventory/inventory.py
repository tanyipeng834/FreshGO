import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('inventory_URL') or "mysql+mysqlconnector://root@localhost:3306/inventory"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# set dbURL=mysql+mysqlconnector://root@localhost:3306/inventory
#docker run --name inventory --network my-net -e inventory_URL=mysql+mysqlconnector://is213@host.docker.internal:3306/inventory mosengtim2021/inventory:1.0	


db = SQLAlchemy(app)


class Inventory(db.Model):
    __tablename__ = 'inventory'
    name = db.Column(db.String(15), nullable=False, primary_key=True)
    quantity = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(15), nullable=False)

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        if self.quantity <= 10:
            self.status = "low"
        elif self.quantity <= 15:
            self.status = "medium"
        else:
            self.status = "high"

    def json(self):
        return {"CropName": self.name, "Quantity": self.quantity, "Status": self.status}
    

@app.route("/inventory", methods=["GET", "POST", "PUT"])
def get_all_crops():
    if request.method == "GET":

        inventory = Inventory.query.all()
        if len(inventory):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "inventory": [crop.json() for crop in inventory]
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There are no crops."
            }
        ), 404
    elif request.method=="POST":
        # This will allow the farmer to create a crop in the database
        data = request.get_json()
        # crop_name = data['name']
        crop_name = data['name']
        # Check if there is a crop with a similar name in the database
        if not (Inventory.query.filter_by(name=crop_name).first()):
            # Create a new object based on the input
            crop = Inventory(**data)
            print(crop)
            try:
                db.session.add(crop)
                db.session.commit()
            except:
                return jsonify(
                    {
                        "code": 500,
                        "data": {
                            "Crop Name": data['name']
                        },
                        "message": "An error occurred creating the Inventory."
                    }
                ), 500

            return jsonify(
                {
                    "code": 201,
                    "data": crop.json()
                }
            )
        else:
            return jsonify(
                {
                    "code": 400,
                    "data": {
                        "Crop Name": data['name']
                    },
                    "message": "Crop Batch already exists."
                }
            ), 400
    elif request.method=="PUT":
        # Check if there is a crop with a similar name in the database
        data = request.get_json()
        crop_name = data['name']
        if (Inventory.query.filter_by(name=crop_name).first()):
            # Create a new object based on the input
            details = Inventory.query.filter_by(name=crop_name).first()
            data['quantity'] = data['quantity'] + details.quantity
            crop = Inventory(**data)

            try:
                db.session.delete(details)
                db.session.commit()
                db.session.add(crop)
                db.session.commit()
            except:
                return jsonify(
                    {
                        "code": 500,
                        "data": {
                            "Crop Name": data['name']
                        },
                        "message": "An error occurred when updating the Inventory."
                    }
                ), 500

            return jsonify(
                {
                    "code": 201,
                    "data": crop.json()
                }
            )
        else:
            return jsonify(
                {
                    "code": 400,
                    "data": {
                        "Crop Name": data['name']
                    },
                    "message": "Crop Batch doesn't exists."
                }
            ), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
