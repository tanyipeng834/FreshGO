#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import and_, func
import os
from datetime import datetime
from datetime import timedelta

from invokes import invoke_http

import amqp_setup
import pika
from threading import Thread
from queue import Queue
import json

# Create a shared queue to store the data returned by the callback function
data_queue = Queue()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'dbURL') or 'mysql+mysqlconnector://root@localhost:3306/purchase_activity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Purchase_Activity(db.Model):
    __tablename__ = 'purchase_activity'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    customer_location = db.Column(db.String, nullable=False)
    transaction_amount = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default='Completed', nullable=False)
    created = db.Column(db.DateTime, default=datetime.now,
                        nullable=False, onupdate=datetime.now)

    def json(self):
        dto = {"Purchase ID": self.id, "Customer ID": self.customer_id,
               "Customer Location": self.customer_location, "Transaction Amount": self.transaction_amount,
               "Status": self.status, "Created": self.created}
        dto['crop_purchased'] = []
        for item in self.crop_purchased:
            dto['crop_purchased'].append(item.json())
        return dto


class Crop_Purchased(db.Model):
    __tablename__ = 'crop_purchased'
    order_id = db.Column(db.Integer, nullable=False, primary_key=True)
    crop_name = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    purchase_id = db.Column(db.ForeignKey(
        'purchase_activity.id', ondelete='cascade', onupdate='cascade'), nullable=False, index=True)
    purchase_activity = db.relationship('Purchase_Activity',
                                        primaryjoin="Crop_Purchased.purchase_id==Purchase_Activity.id", backref='crop_purchased')

    # def __init__(self, crop_id, quantity):
    #     self.crop_id=crop_id
    #     self.quantity=quantity

    def json(self):
        return {"Order ID": self.order_id, "Crop Name": self.crop_name, "Quantity": self.quantity, "Purchase ID": self.purchase_id}


@app.route("/purchase_request", methods=['POST'])
def create_request():
    print(request.get_json())
    cart_item = request.json.get('cart_item')
    customer_location = request.json.get('customer_location')
    print(customer_location)
    customer_phone = request.json.get('customer_phone')
    customer_name = request.json.get('customer_name')
    customer_id = request.json.get('customer_id')
    transaction_amt = request.json.get('transaction_amt')
    delivery_details = {"customer_name": customer_name,
                        "customer_phone": customer_phone, "customer_location": customer_location}
    # invoke the delivery microservice
    delivery_response = invoke_http(
        'http://delivery:5008/delivery', method="POST", json=delivery_details)
    print(delivery_response)
    delivery_amt = delivery_response['delivery_fee']
    transaction_amt = transaction_amt + delivery_amt

    # We will get the
    create_request = Purchase_Activity(
        customer_id=customer_id, customer_location=customer_location, transaction_amount=transaction_amt)

    for item in cart_item:
        crop_name = item['name']
        quantity = item['orderNo']
        price = item['price']
        create_request.crop_purchased.append(Crop_Purchased(
            crop_name=crop_name, quantity=quantity))
        quantity = quantity*-1

        # Update the data base with price also
        purchase_item = {"name": crop_name,
                         "quantity": quantity, "price": price, "type": "vegetable"}
        update_response = invoke_http(
            'http://inventory:5000/inventory', method="PUT", json=purchase_item)
        print(update_response)

    try:
        db.session.add(create_request)
        print(create_request.json())
        db.session.commit()
        payment = stripe(json.loads(
            '{"transaction_amt":'+str(transaction_amt)+'}'))
        if payment['Payment Status'] != 'Success':
            return jsonify(
                {"code": 500,
                    "data":
                    payment,
                    "message": "An error occurred creating the payment."
                 }
            )

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data":
                create_request.json(),
                "message": "An error occurred creating the purchase request." + str(e)
            }
        ), 500
    print("Order Confirmed, Looking for Driver")
    delivery_thread = Thread(target=consume_delivery_messages)
    delivery_thread.start()

    # Block the main thread until the delivery message is received
    delivery_thread.join()

    body = data_queue.get()

    return jsonify({

        "code": 201,
        "data": body,
        "message": "Delivery Staff has accepted the request"
    }), 201


def consume_delivery_messages():
    # Set up the channel to consume messages from the Delivery_Staff queue
    amqp_setup.channel.basic_consume(
        queue='Delivery_Staff', on_message_callback=callback, auto_ack=True)
    # Start consuming messages from the queue
    amqp_setup.channel.start_consuming()


def callback(ch, method, properties, body):

    body = body.decode()
    print(body)
    data_queue.put(body)
    amqp_setup.channel.stop_consuming()

    # message=[cart_item,customer_location]
    # amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="delivery.request",
    #         body=message, properties=pika.BasicProperties(delivery_mode = 2))
    # print("\nDelivery Request published to RabbitMQ Exchange.\n")


def stripe(transaction_amount):
    payment_result = invoke_http(
        "http://checkout:4242/create-payment-intent", method="POST", json=transaction_amount)
    return payment_result


@app.route("/purchase_request")
def get_all():
    if request.is_json:
        data = request.get_json()
        filter_after = datetime.today()-timedelta(days=30)
        print(filter_after)

        requestlist = Purchase_Activity.query.filter(
            Purchase_Activity.created > filter_after).all()
        if len(requestlist):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "Purchase Requests": [order.json() for order in requestlist]
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There are no orders."
            }
        ), 404
    else:
        requestlist = Purchase_Activity.query.all()
        if len(requestlist):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "Purchase Requests": [order.json() for order in requestlist]
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There are no orders."
            }
        ), 404


@app.route("/purchase_request/<int:id>")
def find_by_order_id(id):
    order = Purchase_Activity.query.filter_by(id=id).first()
    if order:
        return jsonify(
            {
                "code": 200,
                "data": order.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "id": id
            },
            "message": "Order not found."
        }
    ), 404


@app.route("/purchase_request/<string:name>")
# Return the sales history of the crop in the past month
def find_by_crop_name(name):
    try:
        one_month_ago = datetime.now() - timedelta(days=30)
        crop_sales_history = Crop_Purchased.query.join(Purchase_Activity).filter(
            Crop_Purchased.crop_name == name,
            Purchase_Activity.created >= one_month_ago
        ).all()
        total_sales = 0
        if crop_sales_history:

            for crop in crop_sales_history:
                total_sales += crop.quantity

            return jsonify(
                {
                    "code": 200,
                    "Total Sales": total_sales
                }
            )
        return jsonify(
            {
                "code": 404,
                "data": {
                    "sales": total_sales
                },
                "message": "crop_sales_history not found."
            }
        ), 404
    except Exception as e:
        return jsonify({"message": str(e)})


@app.route("/purchase_request/update/<int:id>", methods=['PUT'])
def update_order(id):
    try:
        order = Purchase_Activity.query.filter_by(id=id).first()
        if not order:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "order_id": id
                    },
                    "message": "Order not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if 'status' in data:
            order.status = data['status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": order.json()
                }
            ), 200
    except Exception as e:
        print(type(data['status']))
        return jsonify(
            {
                "code": 500,
                "data": {
                    "order_id": id
                },
                "message": "An error occurred while updating the order. " + str(e)
            }
        ), 500


@app.route("/purchase_request/delete/<int:id>", methods=['DELETE'])
def delete_order(id):
    try:
        order1 = Crop_Purchased.query.filter_by(purchase_id=id).all()
        order = Purchase_Activity.query.filter_by(id=id).first()
        if not order:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "order_id": id
                    },
                    "message": "Order not found."
                }
            ), 404
        for o in order1:
            db.session.delete(o)
        db.session.delete(order)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "data": {
                    "order_id": id
                },
                "message": "Order successfully deleted."
            }
        ), 200

    except Exception as e:

        order1 = Crop_Purchased.query.filter_by(purchase_id=id).all()
        print(order1)
        return jsonify(
            {
                "code": 500,
                "data": {
                    "order_id": id
                },
                "message": "An error occurred while deleting the order. " + str(e)
            }
        ), 500


# execute this program only if it is run as a script (not by 'import')
if __name__ == "__main__":
    print("This is flask for " + os.path.basename(__file__) + ": recording logs ...")
    app.run(host='0.0.0.0', port=5006, debug=True)
    print("Goodbye~")


#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script
