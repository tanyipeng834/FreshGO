import requests
from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression

# Initialize Flask app
app = Flask(__name__)

CORS(app)

# Route for the machine learning recommendation
@app.route('/recommend', methods=['POST'])
def predict_height():
    # Get data from microservice in JSON format
    crop_data = request.get_json()
    
    # Extract relevant data
    X = [[d['Crop Fertiliser'], d['Crop Water Level']] for d in crop_data if d['Crop Batch'] == 'Batch A']
    y = [d['Crop Height'] for d in crop_data if d['Crop Batch'] == 'Batch A']
    
    # Perform multiple regression
    model = LinearRegression().fit(X, y)
    
    # Get 5 day weather data forecast from API
    weather_api_key = '83a0602a6cc54cfb88774e7f14326359'
    lat = '1.3521'
    lon = '103.8198'
    weather_api_url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={weather_api_key}'
    weather_data = requests.get(weather_api_url).json()
    humidity = weather_data['main']['humidity']
    
    # Adjust water level recommendation based on humidity
    if humidity > 80:
        recommended_water_level = X[0][1] - 10
    else:
        recommended_water_level = X[0][1]
    
    # Calculate optimal fertiliser recommendation
    recommended_fertiliser = (model.predict([[0, recommended_water_level]])[0] - model.intercept_) / model.coef_[0]
    
    # Calculate maximum height and corresponding fertiliser recommendation
    max_height = model.predict([[recommended_fertiliser, recommended_water_level]])[0]
    
    # Return recommendations
    return jsonify({'recommended_fertiliser': recommended_fertiliser, 'recommended_water_level': recommended_water_level, 'max_height': max_height})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)