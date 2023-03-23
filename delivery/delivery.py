import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import amqp_setup
import pika
from invokes import invoke_http


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'inventory_URL') or "mysql+mysqlconnector://root@localhost:3306/delivery"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# set dbURL=mysql+mysqlconnector://root@localhost:3306/inventory
# docker run --name inventory --network my-net -e inventory_URL=mysql+mysqlconnector://is213@host.docker.internal:3306/inventory mosengtim2021/inventory:1.0

monitorBindingKey = '*.delivery'
db = SQLAlchemy(app)


class Delivery(db.Model):
    __tablename__ = 'delivery'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    customer_name = db.Column(db.String(15), nullable=False)
    customer_location = db.Column(db.String(15), nullable=False)
    # May not need batch for customer not important only needed for farmer
    customer_phone = db.Column(db.String(15), nullable=False)
    # Add the init method into the class
    # def __init__(self, name, shell_life, price, quantity, height, type):
    #     self.name = name
    #     self.shell_life =shell_life
    #     self.price = price
    #     self.quantity = quantity
    #     self.height = height
    #     self.type = type

    def __init__(self, customer_name, customer_location, customer_phone):
        self.customer_name = customer_name
        self.customer_location = customer_location
        self.customer_phone = customer_phone

    def json(self):
        return {"Customer Name": self.customer_name, "Customer Location": self.customer_location, "Customer Phone Number": self.customer_phone}


@app.route("/delivery", methods=["GET", "POST"])
def get_all_deliveries():
    if request.method == 'GET':

        deliveries = Delivery.query.all()
        if len(deliveries):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "inventory": [delivery.json() for delivery in deliveries]
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
        # crop_name = data['name']

        # Check if there is a crop with a similar name in the database
        # Create a new object based on the input
        delivery = Delivery(**data)

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
                "data": delivery.json()
            }
        )


@app.route("/delivery/<int:delivery_id>/<int:staff_id>", methods=["DELETE"])
def delete_delivery(delivery_id,staff_id):

    deliveries = Delivery.query.filter_by(id == delivery_id)
    if len(deliveries):

        Delivery.query.filter_by(id == delivery_id).delete()
        #Invoke http
        # Publish the de
        staff = invoke_http(f'http://127.0.0.1:5003/{staff_id}','POST')
        # Publis the message into amqp queue 
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="staff.delivery", 
            body=staff.json(), properties=pika.BasicProperties(delivery_mode = 2)) 
        return jsonify(
            {
                "code": 200,
                "message": "Entry has been succesfully deleted"
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no such delivery to be deleted."
        }
    ), 404


def receiveRequest():
    amqp_setup.check_setup()

    queue_name = "Delivery_Staff"

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    # an implicit loop waiting to receive messages;
    amqp_setup.channel.start_consuming()
    # it doesn't exit by default. Use Ctrl+C in the command window to terminate it.


# required signature for the callback; no return
def callback(channel, method, properties, body):
    print("\nReceived an error by " + __file__)
    processDelivery(body)
    print()  # print a new line feed


def processDelivery(errorMsg):
    print("Printing the error message:")
    try:
        error = json.loads(errorMsg)
        print("--JSON:", error)
    except Exception as e:
        print("--NOT JSON:", e)
        print("--DATA:", errorMsg)
    print()

    # Use an inner join to connect both the measurements and the input
    # Now we will create a crop object
if __name__ == '__main__':
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    receiveRequest()

    app.run(host='0.0.0.0', port=5005, debug=True)
