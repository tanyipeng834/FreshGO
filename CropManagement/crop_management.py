from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from datetime import datetime
from invokes import invoke_http

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or "mysql+mysqlconnector://root@localhost:3306/crop_management"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Crop class to map to the crops table


class Crop(db.Model):
    __tablename__ = 'crop'
    batch = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), primary_key=True)
    height = db.Column(db.Float, nullable=False)
    water_used = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    fertiliser_used = db.Column(db.Float, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now,
                        nullable=False, onupdate=datetime.now)

    def __init__(self, batch, name, height, water_used, fertiliser_used, quantity):
        self.batch = batch
        self.name = name
        self.height = height
        self.water_used = water_used
        self.fertiliser_used = fertiliser_used
        self.quantity = quantity

    def json(self):
        return {"batch": self.batch, "name": self.name, "height": self.height, "water": self.water_used, "fertiliser": self.fertiliser_used, "quantity": self.quantity}

# Define the route for receiving input from the farmer UI


@app.route('/crop_management', methods=['POST', 'GET', 'DELETE','PUT'])
def manage_crop():
    # Extract input data from POST request
    if request.method == "GET":
        crop_batches = Crop.query.all()
        if len(crop_batches):
            return jsonify(
                {
                    "code": 200,
                    "data": [crop_batch.json() for crop_batch in crop_batches]
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There are no ongrowing crop batches."
            }
        ), 404

    elif request.method == "POST":
        # Check if there is a crop batch with the name , if not create a new batch with
        data = request.get_json()
        crop_name = data["name"]
        crop_height = data["height"]
        crop_water = data["water"]
        crop_fertiliser = data["fertiliser"]
        crop_quantity = data["quantity"]
        crop = Crop.query.filter_by(name=crop_name).order_by(
            Crop.batch.desc()).first()
        if crop:
            new_batch = crop.batch + 1
        else:
            new_batch = 1
        new_crop = Crop(batch=new_batch, name=crop_name, height=crop_height,
                        water_used=crop_water, fertiliser_used=crop_fertiliser, quantity=crop_quantity)
        try:
            db.session.add(new_crop)
            db.session.commit()

        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "Crop Batch": data['name']
                    },
                    "message": "An error occurred creating the Crop Batch."
                }
            ), 500

        return jsonify(
            {
                "code": 201,
                "data": new_crop.json()
            }
        )
    elif request.method=="DELETE":
        data = request.get_json()
        print(data)
        batch = data["batch"]
        name = data["name"]
        # harvest the crops from the farmer POV
        crop_batch = Crop.query.filter_by(batch=batch, name=name).first()
        quantity = crop_batch.quantity
        print(quantity)
        if crop_batch:
            try:
                db.session.delete(crop_batch)
                db.session.commit()
            except:
                return jsonify(
                    {
                        "code": 500,
                        "data": {
                            "Crop Batch": data['name']
                        },
                        "message": "An error occurred deleting the Crop Batch."
                    }
                ), 500
            update_json = {
                "name": name,
                "quantity": quantity,
                "price": 1.20,
                "type": "vegetable"
            }
            response = invoke_http(
                f'http://inventory:5000/inventory', "PUT", update_json)
            return jsonify(
                {
                    "code": 200,
                    "message": "Harvested the crops Succesfully"
                }
            )

        else:
            return jsonify(
                {
                    "code": 404,
                    "message": "There are no ongrowing crop batches."
                }
            ), 404
    else:
        data = request.get_json()
        
        batch = data["batch"]
        name = data["name"]
        height = data["height"]
        crop = Crop.query.filter_by(name=name, batch=batch).first()
        if crop:
            crop.height = height
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "message": "Crop Height has been  updated Succesfully"
                }
            )
        else:
            return jsonify(
        {
            "code": 404,
            "message": "There are no ongrowing crop batches with that batch name."
        }
    ), 404









@app.route('/crop_management/<string:name>', methods=['GET'])
def get_batch_by_name(name):
    crop_batches = Crop.query.filter_by(name=name).all()
    if len(crop_batches):
        return jsonify(
            {
                "code": 200,
                "data": [crop_batch.json() for crop_batch in crop_batches]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no ongrowing crop batches with that batch name."
        }
    ), 404


# Add another route for them to update the height



# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
