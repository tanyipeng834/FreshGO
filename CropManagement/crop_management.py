from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import requests

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define Crop model
class Crop(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    batch = db.Column(db.Integer, primary_key=True)
    water_used = db.Column(db.Float, nullable=False)
    fertiliser_used = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    date_planted = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'name': self.name,
            'batch': self.batch,
            'water_used': self.water_used,
            'fertiliser_used': self.fertiliser_used,
            'height': self.height,
            'date_planted': self.date_planted
        }

# Define endpoint to get crop data and recommendation
@app.route('/crop/<name>/<batch>', methods=['GET'])
def get_crop(name, batch):
    # Get crop data from inventory microservice
    inventory_service_url = environ.get('isURL')
    response = requests.get(f'{inventory_service_url}/inventory/{name}/{batch}')
    if response.status_code != 200:
        return jsonify({'message': 'Failed to get crop data from inventory microservice'}), 500
    crop_data = response.json()

    # Get recommendation from machine learning microservice
    ml_service_url = environ.get('mlURL')
    ml_data = {
        'water_used': crop_data['water_used'],
        'fertiliser_used': crop_data['fertiliser_used'],
        'height': crop_data['height']
    }
    response = requests.post(ml_service_url, json=ml_data)
    if response.status_code != 200:
        return jsonify({'message': 'Failed to get recommendation from machine learning microservice'}), 500
    recommendation = response.json()

    # Initializing an empty dictionary that we will later use to build the response data.
    data = {
        'water_used': crop_data['water_used'],
        'fertiliser_used': crop_data['fertiliser_used'],
        'height': crop_data['height'],
        'date_planted': crop_data['date_planted'],
        'current_height': recommendation['current_height'],
        'recommended_water': recommendation['recommended_water'],
        'recommended_fertiliser': recommendation['recommended_fertiliser']
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
