from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import requests
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class CropData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    water_level = db.Column(db.Integer, nullable=False)
    fertiliser = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(50), nullable=False)

class CropManagementService:
    def __init__(self, crop_id):
        self.crop_id = crop_id

# handle incoming requests to set new water and update the database
    def setNewWater(self, new_water_level):
        crop_data = CropData.query.get(self.crop_id)
        crop_data.water_level = new_water_level
        crop_data.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.session.commit()

# handle incoming requests to set new fertiliser and update the database
    def setNewFertiliser(self, new_fertiliser_usage):
        crop_data = CropData.query.get(self.crop_id)
        crop_data.fertiliser = new_fertiliser_usage
        crop_data.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.session.commit()

@app.route('/set_new_water', methods=['POST'])
def set_new_water():
    crop_id = request.json['crop_id']
    new_water_level = request.json['new_water_level']

    crop_service = CropManagementService(crop_id)
    crop_service.setNewWater(new_water_level)

    return jsonify({'status': 'success'})

@app.route('/set_new_fertiliser', methods=['POST'])
def set_new_fertiliser():
    crop_id = request.json['crop_id']
    new_fertiliser_usage = request.json['new_fertiliser_usage']

    crop_service = CropManagementService(crop_id)
    crop_service.setNewFertiliser(new_fertiliser_usage)

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
