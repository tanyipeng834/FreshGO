from flask import Flask, jsonify
import requests
from twilio.rest import Client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Fetch farmer phone number from microservice
def get_farmer_phone():
    response = requests.get("http://127.0.0.1:5003/type/farmer")
    data = response.json()
    return data["data"][0]["phone"]

# Send SMS function


def send_sms(to, body):
    account_sid = 'AC486de2818db6343a04d676fcfff76649'
    auth_token = '8053127dfb967c94a7d521d9fd76eac2'
    client = Client(account_sid, auth_token)
    to = "+65 " + to
    print(to)

    message = client.messages \
        .create(
            body=body,
            from_='+14344258543',
            to=to
        )

    print("Message sent to: " + message.to)

# Endpoint to fetch crop data and send SMS to farmer if status is "Low"


@app.route('/check_status', methods=['GET'])
def check_status():
    response = requests.get("http://127.0.0.1:5000/inventory")
    data = response.json()
    inventory = data["data"]["inventory"]
    for item in inventory:
        if item["status"] == "Low":
            farmer_phone = get_farmer_phone()
            message = f"The status of {item['name']} is {item['status']}. Current quantity: {item['quantity']}. Please take necessary action."
            send_sms(farmer_phone, message)
    return jsonify({"message": "Status checked."})
# # Twilio account credentials
# account_sid = 'AC486de2818db6343a04d676fcfff76649'
# auth_token = '8053127dfb967c94a7d521d9fd76eac2'
# client = Client(account_sid, auth_token)

# # Endpoint for sending SMS
# @app.route('/send-sms')
# def send_sms():
#     # Get inventory data from other microservice
#     inventory_data = requests.get('http://127.0.0.1:5000/inventory').json()
#     if inventory_data["code"] == 200:
#         # Loop through inventory data and send SMS if status is low
#         for item in inventory_data["data"]["inventory"]:
#             if item["status"] == "Low":
#                 message = client.messages \
#                     .create(
#                         body=f"Low stock for {item['name']}. Current quantity: {item['quantity']}",
#                         from_='+14344258543',
#                         to=''
#                     )
#                 print(message.sid) # print SMS ID to console
#         return "SMS Sent"
#     else:
#         return "Error retrieving inventory data"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
