from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Crop class to map to the crops table
class Crop(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    batch = db.Column(db.String(50), primary_key=True)
    current_water_used = db.Column(db.Float, nullable=False)
    recommended_water_level = db.Column(db.Float, nullable=False)
    recommended_fertilizer_amount = db.Column(db.Float, nullable=False)

# Define the route for receiving input from the farmer UI
@app.route('/crop_management', methods=['POST'])
def manage_crop():
    # Extract input data from POST request
    crop_name = request.json.get('name')
    batch = request.json.get('batch')
    current_water_used = request.json.get('current_water_used')
    
    # Query inventory microservice for crop data
    inventory_data = request.get('http://127.0.0.1:5000/inventory/crop/' + crop_name + '/' + batch).json()
    # Call machine learning microservice to get recommended water level and fertilizer amount
    recommended_data = request.post('http://127.0.0.1:5002/machine_learning/recommend', json=inventory_data).json()
    
    # Update Crop object in database
    crop = Crop.query.filter_by(name=crop_name, batch=batch).first()
    crop.current_water_used = current_water_used
    crop.recommended_water_level = recommended_data['recommended_water_level']
    crop.recommended_fertilizer_amount = recommended_data['recommended_fertilizer_amount']
    db.session.commit()
    
    return jsonify({
        'message': 'Crop management data updated successfully.'
    }), 200

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
