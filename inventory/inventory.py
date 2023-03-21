from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# set dbURL=mysql+mysqlconnector://root@localhost:3306/inventory


db = SQLAlchemy(app)


class Inventory(db.Model):
    __tablename__ = 'inventory'
    name = db.Column(db.String(15), nullable=False, primary_key=True)
    shell_life = db.Column(db.String(15), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float(precision=2))
    date = db.Column(db.Date)
    # May not need batch for customer not important only needed for farmer
    batch = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(15), nullable=False)

    # Add the init method into the class
    # def __init__(self, name, shell_life, price, quantity, height, type):
    #     self.name = name
    #     self.shell_life =shell_life
    #     self.price = price
    #     self.quantity = quantity
    #     self.height = height
    #     self.type = type

    def json(self):
        return {"CropName": self.name, "Shell Life": self.shell_life, "Price": self.price, "Quantity": self.quantity, "Height": self.height, "Type": self.type}


class CropData(db.Model):
    __tablename__ = 'CropData'
    name = db.Column(db.String(15), db.ForeignKey(
        'inventory.name'), nullable=False, primary_key=True)
    batch = db.Column(db.Integer, db.ForeignKey(
        'inventory.batch'), nullable=False, primary_key=True)
    humidity = db.Column(db.Float(precision=2), nullable=False)
    water = db.Column(db.Float(precision=2), nullable=False)
    fertiliser = db.Column(db.Float(precision=2), nullable=False)
    crop_name = db.relationship("Inventory", foreign_keys=[name])
    crop_batch = db.relationship("Inventory", foreign_keys=[batch])

    def json(self):
        return {"Crop Name": self.name, "Crop Batch": self.batch, "Humidity Levels": self.humidity, "Water Level": self.water, "Fertiliser": self.fertiliser}


class CropMeasurements(db.Model):
    __tablename__ = 'CropMeasurements'
    name = db.Column(db.String(15), db.ForeignKey(
        'inventory.name'), nullable=False, primary_key=True)
    batch = batch = db.Column(db.Integer, db.ForeignKey(
        'inventory.batch'), nullable=False, primary_key=True)
    date_measured = db.Column(db.Date, primary_key=True)
    current_height = db.Column(db.Float(precision=2), nullable=False)
    crop_name = db.relationship("Inventory", foreign_keys=[name])
    crop_batch = db.relationship("Inventory", foreign_keys=[batch])

    def json(self):
        return {"Crop Name": self.name, "Crop Batch": self.batch, "Date Measured": self.date_measured, "Crop Height": self.current_height}


@app.route("/inventory", methods=["GET", "POST"])
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
    else:

        # This will allow the farmer to create a crop in the database
        data = request.get_json()
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
                            "Crop Name": crop_name
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
                        "Crop Name": crop_name
                    },
                    "message": "Crop Batch already exists."
                }
            ), 400


@app.route("/inventory/measurements/<string:crop_name>", methods=["GET"])
def get_crop_measurements(crop_name):
    # Get all the measurements for the crop with crop_name

    # Use an inner join to connect both the measurements and the input
    query = db.session.query(CropMeasurements, CropData).join(CropData, db.and_(
        CropMeasurements.name == CropData.name, CropMeasurements.batch == CropData.batch))
    crops_data = query.filter(CropData.name == crop_name).all()
    if len(crops_data):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Crop Data": [{"Crop Name": crop_measurements.name, "Crop Batch": crop_measurements.batch, "Date Measured": crop_measurements.date_measured, "Crop Height": crop_measurements.current_height, "Crop Humidity": crop_data.humidity, "Crop Water Level": crop_data.water, "Crop Fertiliser": crop_data.fertiliser} for crop_measurements, crop_data in crops_data]
                }
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "There is not mesurements for this crop"

            }

        )


@app.route("/inventory/<string:crop_name>/<string:batch>", methods=["GET", "POST"])
def crop_data_controller(crop_name, batch):
    if request.method == "GET":
        # Get the data for the input parmaters
        crop_data = Inventory.query.filter_by(name=crop_name, batch=batch)
        if len(crop_data):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "Crop Data": crop_data.json()
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": f"There are no data for this ${crop_name} belonging to this ${batch}."
            }
        ), 404
    else:

        # This will allow the farmer to create a crop in the database
        data = request.get_json()
        # Check if there is a crop with a similar name in the database
        if not (CropData.query.filter_by(name=crop_name, batch=batch).first()):
            # Create a new object based on the input
            crop_data = CropData(name=crop_name, batch=batch, **data)

            try:
                db.session.add(crop_data)
                db.session.commit()
            except:
                return jsonify(
                    {
                        "code": 500,
                        "data": {
                            "Crop Name": crop_name,
                            "Crop Batch": batch
                        },
                        "message": f"An error occurred creating batch ${batch} of this ${crop_name}."
                    }
                ), 500

            return jsonify(
                {
                    "code": 201,
                    "data": crop_data.json()
                }
            )
        else:
            return jsonify(
                {
                    "code": 400,
                    "data": {
                        "Crop Name": crop_name,
                        "Crop Batch": batch
                    },
                    "message": "Crop Batch already exists."
                }
            ), 400


@app.route("/inventory/check-inventory", methods=["GET"])
def check_crop_quantity():
    # Get all the measurements for the crop with quantity less than 5
    Inventory.query()

    # Use an inner join to connect both the measurements and the input
    # Now we will create a crop object
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
