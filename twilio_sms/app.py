from flask import Flask
import requests
from twilio.rest import Client

app = Flask(__name__)

# Twilio account credentials
account_sid = 'AC486de2818db6343a04d676fcfff76649'
auth_token = '8053127dfb967c94a7d521d9fd76eac2'
client = Client(account_sid, auth_token)

# Endpoint for sending SMS
@app.route('/send-sms')
def send_sms():
    # Get inventory data from other microservice
    inventory_data = requests.get('http://127.0.0.1:5000/inventory').json()
    if inventory_data["code"] == 200:
        # Loop through inventory data and send SMS if status is low
        for item in inventory_data["data"]["inventory"]:
            if item["status"] == "Low":
                message = client.messages \
                    .create(
                        body=f"Low stock for {item['name']}. Current quantity: {item['quantity']}",
                        from_='+14344258543',
                        to='+6593486088'
                    )
                print(message.sid) # print SMS ID to console
        return "SMS Sent"
    else:
        return "Error retrieving inventory data"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)