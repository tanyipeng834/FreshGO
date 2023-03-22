#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from datetime import datetime
import json 
from invokes import invoke_http
import profile.amqp_setup as amqp_setup
import pika

# book_URL = "http://localhost:5000/book"
# shipping_record_URL = "http://localhost:5002/shipping_record"
# activity_log_URL = "http://localhost:5003/activity_log"
# error_URL = "http://localhost:5004/error"

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+mysqlconnector://root@localhost:3306/purchase_activity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Purchase_Activity(db.Model):
    __tablename__ = 'purchase_activity'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    customer_location = db.Column(db.Integer)
    status = db.Column(db.String, default='New/Ongoing', nullable = False)
    created = db.Column(db.DateTime, default=datetime.now, nullable=False, onupdate=datetime.now)

    def json(self):
        dto={"Purchase ID": self.id, "Customer ID": self.customer_id,
                "Customer Location": self.customer_location, 
                "Status": self.status, "Created": self.created}
        dto['crop_purchased']=[]
        for item in self.crop_purchased:
            dto['crop_purchased'].append(item.json())
        return dto
    
class Crop_Purchased(db.Model):
    __tablename__ = 'crop_purchased'
    id = db.Column(db.Integer, nullable = False, primary_key=True)
    crop_id = db.Column(db.Integer, nullable = False)
    quantity=db.Column(db.Integer, nullable=False)
    purchase_id = db.Column(db.ForeignKey('purchase_activity.id',ondelete='cascade',onupdate='cascade'), nullable = False, index=True)
    purchase_activity=db.relationship('Purchase_Activity', 
                                      primaryjoin= "Crop_Purchased.purchase_id==Purchase_Activity.id", backref='crop_purchased')

    # def __init__(self, crop_id, quantity):
    #     self.crop_id=crop_id
    #     self.quantity=quantity

    def json(self):
        return {"ID": self.id, "Crop ID": self.crop_id, "Quantity":self.quantity, "Purchase ID": self.purchase_id}



@app.route("/purchase_request", methods=['POST'])
def create_request():
    cart_item=request.json.get('cart_item')
    customer_id = request.json.get('customer_id')
    customer_location = request.json.get('customer_location')
    create_request = Purchase_Activity(customer_id=customer_id, customer_location=customer_location)
    for item in cart_item:
        create_request.crop_purchased.append(Crop_Purchased(crop_id=item['crop_id'], quantity=item['quantity']))
    
        
    try:
        db.session.add(create_request)
        print(create_request.json())
        db.session.commit()
        
    except Exception as e:
        return jsonify(
                    {
                    "code": 500,
                    "data": 
                    create_request.json()
                    ,
                    "message": "An error occurred creating the purchase request." + str(e)
                    }
                ), 500 
    #invoke stripe api here
    # if sucesss  send message to deliveyr api then return code 200
    
    print (jsonify(
        {  "code": 201,
        "data": create_request.json()
        }
        ))
    

    # Send the message in json
    message=[cart_item,customer_location]
    delivery_reply = amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="delivery.request", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
    print("\nDelivery Request published to RabbitMQ Exchange.\n")
   
@app.route("/purchase_request")
def get_all():
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
        order1=Crop_Purchased.query.filter_by(purchase_id=id).all()
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
        
        order1=Crop_Purchased.query.filter_by(purchase_id=id).all()
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
    





if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("This is flask for " + os.path.basename(__file__) + ": recording logs ...")
    app.run(host='0.0.0.0', port=5000, debug=True)
    print("Goodbye~")


#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

