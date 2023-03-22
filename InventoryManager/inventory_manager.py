from invokes import invoke_http
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import sys
from os import environ
import json


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('inventory_manager_URL') or "mysql+mysqlconnector://root@localhost:3306/inventory_manager"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#docker run --name inventory_manager --network my-net -e inventory_manager_URL=mysql+mysqlconnector://is213@host.docker.internal:3306/inventory_manager mosengtim2021/inventory_manager:1.0	

# This will be the code for the farmer
inventory_URL = "http://localhost:5000/inventory" 

db = SQLAlchemy(app)
class Growth(db.Model):
    __tablename__ = 'Growth'
    id = db.Column(db.Integer, primary_key=True)
    farmer = db.Column(db.String(30), nullable=False)
    crop = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date_grown = db.Column(db.Date, nullable=False)
    date_harvested = db.Column(db.Date, nullable=False)

    def __init__(self, farmer, crop, quantity, date_grown, date_harvested):
        self.farmer = farmer
        self.crop = crop
        self.quantity = quantity
        self.date_grown = date_grown
        self.date_harvested = date_harvested

    def json(self):
        return {"id": self.id, "crop": self.crop, "quantity": self.quantity, "date_grown": self.date_grown, "date_harvested": self.date_harvested}
    
@app.route("/manager", methods=['POST', 'GET'])
def place_order():
    # Simple check of input format and data of the request are JSON
    if request.method == "POST":
        if request.is_json:
            try:
                data = request.get_json()
                print("\nReceived an batch order in JSON:", data)

                # do the actual work
                # 1. Send harvested batch
                result = processBatch(data, request.method)
                print('\n------------------------')
                print('\nresult: ', result)
                return jsonify(result), result["code"]

            except Exception as e:
                # Unexpected error in code
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
                print(ex_str)

                return jsonify({
                    "code": 500,
                    "message": "inventory.py internal error: " + ex_str
                }), 500
            
        # if reached here, not a JSON request.
        return jsonify({
            "code": 400,
            "message": "Invalid JSON input: " + str(request.get_data())
        }), 400
    else:
        try:
            # 1. Send request
            data = []
            result = processBatch(data, request.method)
            print('\n------------------------')
            print('\nresult: ', result)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "inventory.py internal error: " + ex_str
            }), 500

def processBatch(data, method):
    # Send the batch info to inventory
    # Invoke the inventory MS
    print('\n-----Invoking inventory microservice-----')
    URL = inventory_URL
    print(URL)
    order_result = invoke_http(URL, method=method, json=data)
    print('order_result:', order_result)

    # Check the order result;
    code = order_result["code"]
    message = json.dumps(order_result)

    if code not in range(200, 300):
        return {
            "code": 500,
            "data": {"order_result": order_result},
            "message": "Batch insert failed."
        }

    return {
        "code": 201,
        "data": {
            "order_result": order_result,
        }
    }



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)

