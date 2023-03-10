from flask import Flask, jsonify, request

app = Flask(__name__)

class CropManagementService:
    def __init__(self, water_level, fertiliser_usage, date, crop_id):
        self.water_level = water_level
        self.fertiliser_usage = fertiliser_usage
        self.date = date
        self.crop_id = crop_id

    def set_new_water(self, new_water_level):
        self.water_level = new_water_level

    def set_new_fertiliser(self, new_fertiliser_usage):
        self.fertiliser_usage = new_fertiliser_usage

#initial values for the water level, fertiliser usage, date, and crop ID.
crop_data = CropManagementService(50, 10, "2023-03-10", 1)

#Returns the current state of the crop data.
@app.route('/', methods=['GET'])
def get_crop_data():
    return jsonify({
        'water_level': crop_data.water_level,
        'fertiliser_usage': crop_data.fertiliser_usage,
        'date': crop_data.date,
        'crop_id': crop_data.crop_id
    })

# Accepts a new water level value in JSON format and updates the water_level property of the CropManagementService instance.
@app.route('/set_new_water', methods=['PUT'])
def set_new_water():
    data = request.get_json()
    crop_data.set_new_water(data['new_water_level'])
    return 'Water level updated successfully', 200

#Accepts a new fertiliser usage value in JSON format and updates the fertiliser_usage property of the CropManagementService instance.
@app.route('/set_new_fertiliser', methods=['PUT'])
def set_new_fertiliser():
    data = request.get_json()
    crop_data.set_new_fertiliser(data['new_fertiliser_usage'])
    return 'Fertiliser usage updated successfully', 200

if __name__ == '__main__':
    app.run(debug=True)
