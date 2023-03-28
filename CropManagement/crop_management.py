from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or "mysql+mysqlconnector://root@localhost:3306/crop_management"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Crop class to map to the crops table
class Crop(db.Model):
    __tablename__ = 'crop'
    batch =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), primary_key=True)
    height = db.Column(db.Float, nullable=False)
    water_used = db.Column(db.Float, nullable=False)
    fertiliser_used = db.Column(db.Float, nullable=False)
    
    
    def __init__(self, batch, name, height, water_used, fertiliser_used):
        self.batch = batch
        self.name = name
        self.height = height
        self.water_used = water_used
        self.fertiliser_used = fertiliser_used

    def json(self):
        return {"Batch": self.batch, "Name": self.name,"Height":self.height, "Water Used": self.water_used, "Fertiliser Used": self.fertiliser_used}

# Define the route for receiving input from the farmer UI
@app.route('/crop_management', methods=['POST'])
def manage_crop():
    # Extract input data from POST request
    crop_name = request.json.get('name')
    current_water_used = request.json.get('current_water_used')
    
    # Query inventory microservice for crop data
    inventory_data = request.get('http://127.0.0.1:5000/inventory/measurements/' + crop_name).json()
    # Call machine learning microservice to get recommended water level and fertiliser amount
    recommended_data = request.post('http://127.0.0.1:5002/machine_learning/recommend', json=inventory_data).json()
    
    # Update Crop object in database
    crop = Crop.query.filter_by(name=crop_name).first()
    crop.current_water_used = current_water_used
    crop.recommended_water_level = recommended_data['recommended_water_level']
    crop.recommended_fertiliser = recommended_data['recommended_fertiliser']
    crop.max_height = recommended_data['max_height']
    db.session.commit()
    
    return jsonify({
        'message': 'Crop management data updated successfully.'
    }), 200

@app.route('/crop_managements', methods=['GET', 'PUT', 'POST'])
def managed_crop():
    if request.method == "GET":
        data = Crop.query.all()
        if len(data):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "inventory": [cropx.json() for cropx in data]
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There are no crops."
            }
        ), 404
    elif request.method == "PUT":
        data = request.get_json()
        crop_batch = data['batch']
        crop_name = data['name']
        height = data['height']
        water_used = data['water used']
        fertiliser_used = data['fertiliser used']
        if (Crop.query.filter_by(batch=crop_batch, name=crop_name).first()):
            crop = Crop.query.filter_by(batch=crop_batch, name=crop_name).first()
            crop.height = height
            crop.water_used = water_used
            crop.fertiliser_used = water_used
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
    elif request.method == "POST":
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




# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
