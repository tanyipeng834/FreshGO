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

# book_URL = "http://localhost:5000/book"
# order_URL = "http://localhost:5001/order"
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

    def __init__(self, crop_id, quantity):
        self.crop_id=crop_id,
        self.quantity=quantity

    def json(self):
        return {"ID": self.id, "Crop ID": self.crop_id, 
                "Quantity":self.quantity, "Purchase ID": self.purchase_id}

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
    print("Order Confirmed, Looking for Driver")
    return jsonify(
        {  "code": 201,
        "data": create_request.json()
        }
        ),
   

# @app.route("/purchase_request/order", methods=['GET','POST'])
# def purchase_request(customer_id, delivery_staff_id, customer_location,transaction_amount, status, created):
#     data = request.get_json()
#     #create request for customer's purchase
#     purchase_request = Purchase_Activity(customer_id, delivery_staff_id, customer_location,transaction_amount, status, created,**data)
#     try:
#         db.session.add(purchase_request)
#         db.session.commit()
#     except:
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "Customer_ID": customer_id,
#                     "Delivery Staff":delivery_staff_id,
#                     "Delivery Location":customer_location,
#                     "Transaction Amt":transaction_amount,
#                     "Purchase Request ID": id,
#                     "Customer ID": customer_id,
#                     "Status":status
#                     },
#                 "message": "An error occurred creating the purchase request."
#             }
#         ), 500
#     return jsonify(
#         {  "code": 201,
#             "data": Purchase_Activity.json()
#         }
#     ), 201




if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("This is flask for " + os.path.basename(__file__) + ": recording logs ...")
    app.run(host='0.0.0.0', port=5000, debug=True)
    print("Goodbye~")


#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

