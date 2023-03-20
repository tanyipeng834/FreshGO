import requests
from flask import Flask, jsonify, request
from sklearn.linear_model import LinearRegression

# Initialize Flask app
app = Flask(__name__)

# Define the route for the machine learning recommendation
@app.route('/recommend', methods=['POST'])
def recommend():
    # Extract input data from POST request
    crop_data = request.json
    
    # Query weather API for humidity data
    weather_data = requests.get('http://api.data.gov.sg/v1/environment/24-hour-weather-forecast').json()
    humidity = weather_data['items']
    
    # Calculate recommended water level
    recommended_water_level = calculate_water_level(crop_data, humidity)
    
    # Calculate recommended fertilizer amount
    recommended_fertilizer_amount = calculate_fertilizer_amount(crop_data)
    
    return jsonify({
        'recommended_water_level': recommended_water_level,
        'recommended_fertilizer_amount': recommended_fertilizer_amount
    }), 200

# Function to calculate recommended water level
def calculate_water_level(crop_data, humidity):
    # Extract relevant data from crop_data
    previous_heights = crop_data['previous_heights']
    current_height = crop_data['current_height']
    current_water_used = crop_data['current_water_used']
    
    # Reduce recommended water level if humidity is above 80%
    if humidity > 80:
        recommended_water_level = current_height * 0.7 - current_water_used
    else:
        recommended_water_level = current_height * 0.8 - current_water_used
    
    return recommended_water_level

# Function to calculate recommended fertilizer amount
def calculate_fertilizer_amount(crop_data):
    # Extract relevant data from crop_data
    previous_heights = crop_data['previous_heights']
    current_height = crop_data['current_height']
    
    # Train linear regression model on previous height data
    X = [[i] for i in range(1, len(previous_heights) + 1)]
    y = previous_heights
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict next height using linear regression model
    next_height = model.predict([[len(previous_heights) + 1]])[0]
    
    # Calculate recommended fertilizer amount based on change in height
    fertilizer_amount = (next_height - current_height) * 0.1
    
    return fertilizer_amount

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

