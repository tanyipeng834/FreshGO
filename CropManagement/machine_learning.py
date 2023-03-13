import requests
from flask import Flask, jsonify
from CropManagement import CropManagementService

app = Flask(__name__)

class WaterFertiliserRecommendationService:
    def __init__(self, crop_data_url, weather_api_url):
        self.crop_data_url = crop_data_url
        self.weather_api_url = weather_api_url

    def get_recommended_water(self):
        crop_data = requests.get(self.crop_data_url).json()
        weather_data = requests.get(self.weather_api_url).json()

        # Simple calculation to recommended water level
        recommended_water_level = crop_data['water_level'] + weather_data['waterFall'] - 5

        return recommended_water_level

    def get_recommended_fertiliser(self):
        crop_data = requests.get(self.crop_data_url).json()
        weather_data = requests.get(self.weather_api_url).json()

        # Simple calculation to recommended fertiliser usage
        recommended_fertiliser_usage = crop_data['fertiliser_usage'] + weather_data['waterFall'] / 10

        return recommended_fertiliser_usage

#listens for incoming requests on the specified port
recommendation_service = WaterFertiliserRecommendationService('http://localhost:5000', 'http://weatherapi.com')

#Returns the recommended water level calculated by the machine learning algorithm and sets the new water level in the CropManagementService microservice using the set_new_water method.
@app.route('/get_recommended_water', methods=['GET'])
def get_recommended_water():
    recommended_water_level = recommendation_service.get_recommended_water()
    crop_data = CropManagementService(recommended_water_level, None, None, None)
    crop_data.set_new_water(recommended_water_level)

    return jsonify({
        'recommended_water_level': recommended_water_level
    })

#Returns the recommended fertiliser usage calculated by the machine learning algorithm and sets the new fertiliser usage in the CropManagementService microservice using the set_new_fertiliser method.
@app.route('/get_recommended_fertiliser', methods=['GET'])
def get_recommended_fertiliser():
    recommended_fertiliser_usage = recommendation_service.get_recommended_fertiliser()
    crop_data = CropManagementService(None, recommended_fertiliser_usage, None, None)
    crop_data.set_new_fertiliser(recommended_fertiliser_usage)

    return jsonify({
        'recommended_fertiliser_usage': recommended_fertiliser_usage
    })

if __name__ == '__main__':
    app.run(debug=True)
