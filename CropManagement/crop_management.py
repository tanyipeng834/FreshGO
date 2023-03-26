from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('crop_management_URL') or "mysql+mysqlconnector://root@localhost:3306/crop_management"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Crop class to map to the crops table
class Crop(db.Model):
    __tablename__ = 'crops'
    batch =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    max_height = db.Column(db.Float, nullable=False)
    recommended_water_level = db.Column(db.Float, nullable=False)
    recommended_fertiliser_level = db.Column(db.Float, nullable=False)
    
    def __init__(self, name, max_height):
        self.name = name
        self.max_height = max_height
        self.recommended_water_level = 5
        self.recommended_fertiliser_level = 5

    def json(self):
        return {"Batch": self.batch, "Crop Name": self.name,"Crop Height":self.max_height,"Recommend Water":self.recommended_water_level,"Recommend Fertilliser":self.recommended_fertiliser_level}


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
        crop_height = data['height']
        if (Crop.query.filter_by(batch=crop_batch).first()):
            crop = Crop.query.filter_by(batch=crop_batch).first()
            crop.max_height = crop_height
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




# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
