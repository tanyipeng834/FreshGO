import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import amqp_setup
import pika
from invokes import invoke_http
import requests

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or "mysql+mysqlconnector://root@localhost:3306/deliveries"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# set dbURL=mysql+mysqlconnector://root@localhost:3306/inventory
# docker run --name inventory --network my-net -e inventory_URL=mysql+mysqlconnector://is213@host.docker.internal:3306/inventory mosengtim2021/inventory:1.0

monitorBindingKey = '*.delivery'
db = SQLAlchemy(app)

google_map_key = 'AIzaSyC9IHubhNzjWcBNk5Igv2-xn4WcrCPg9Ig'
factory_location = '102 Henderson Rd'


class Deliveries(db.Model):
    __tablename__ = 'deliveries'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    customer_name = db.Column(db.String(15), nullable=False)
    customer_location = db.Column(db.String(15), nullable=False)
    # May not need batch for customer not important only needed for farmer
    customer_phone = db.Column(db.String(15), nullable=False)
    delivery_charge = db.Column(db.Float, nullable=False)
    # Add the init method into the class
    # def __init__(self, name, shell_life, price, quantity, height, type):
    #     self.name = name
    #     self.shell_life =shell_life
    #     self.price = price
    #     self.quantity = quantity
    #     self.height = height
    #     self.type = type

    def __init__(self, id, customer_name, customer_location, customer_phone, delivery_charge):
        self.id = id
        self.customer_name = customer_name
        self.customer_location = customer_location
        self.customer_phone = customer_phone
        self.delivery_charge = delivery_charge

    def json(self):
        return {"customerName": self.customer_name, "customerLocation": self.customer_location, "customerPhone": self.customer_phone, "deliveryCharge": self.delivery_charge, "id": self.id}


@app.route("/delivery", methods=["GET", "POST"])
def get_all_deliveries():
    if request.method == 'GET':

        deliveries = Deliveries.query.all()
        if len(deliveries):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "delivery": [delivery.json() for delivery in deliveries]
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There are no delivery requests."
            }
        ), 404
    else:

        # This will allow the farmer to create a crop in the database
        data = request.get_json()
        print(data)
        customer_location = data['customer_location']
        # crop_name = data['name']
        params = {'key': google_map_key, 'origins': factory_location,
                  'destinations': customer_location}
        return_json = requests.get(
            'https://maps.googleapis.com/maps/api/distancematrix/json', params=params)
        delivery_distance = return_json.json(
        )['rows'][0]['elements'][0]['distance']['text']
        delivery_distance = float(delivery_distance.strip('km'))
        delivery_fee = round(delivery_distance*0.85, 2)

        # Check if there is a crop with a similar name in the database
        # Create a new object based on the input
        delivery = Deliveries(**data, charge=delivery_fee)

        try:
            db.session.add(delivery)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,

                    "message": "An error occurred creating the Inventory."
                }
            ), 500

        return jsonify(
            {
                "code": 201,
                "data": delivery.json(),
                "delivery_fee": delivery_fee
            }
        )


@app.route("/delivery/delete", methods=["DELETE"])
def delete_delivery():
    data = request.get_json()
    delivery_id = data["deliveryId"]
    staff_id = data["staffId"]
    # Get the first element that match the delivery Id
    print(delivery_id)
    deliveries = Deliveries.query.filter_by(id=delivery_id).first()
    if deliveries:

        Deliveries.query.filter_by(id=delivery_id).delete()
        # Invoke http
        # Publish the delivery microservice to get the staff that will be coming
        staff = invoke_http(f'http://127.0.0.1:5003/{staff_id}', 'GET')
        # Send back the delivery staff that is on the way to collect the delivery
        body = {"deliveryId": delivery_id,
                "staff": staff.json()
                }
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="staff.delivery",
                                         body=body, properties=pika.BasicProperties(delivery_mode=2))
        return jsonify(
            {
                "code": 200,
                "message": "Delivery Request  has been succesfully accepted by "
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no such delivery to be deleted."
        }
    ), 404


# required signature for the callback; no return
    # Use an inner join to connect both the measurements and the input
    # Now we will create a crop object
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
