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
purchase_activity_URL = "http://localhost:5006/purchase_request"

db = SQLAlchemy(app)
    
#CRUD Inventory
@app.route("/manager", methods=['POST', 'GET', 'PUT'])
def place_order():
    # Simple check of input format and data of the request are JSON
    if request.method == "POST":
        if request.is_json:
            try:
                data = request.get_json()
                print("\nReceived an batch order in JSON:", data)

                # do the actual work
                # 1. Send harvested batch
                result = processBatch(data, request.method, inventory_URL)
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
    if request.method == "GET":
        try:
            # 1. Send request
            data = []
            result = processBatch(data, request.method, inventory_URL)
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
    if request.method == 'PUT':
        if request.is_json:
            try:
                data = request.get_json()
                result = processBatch(data, request.method, inventory_URL)
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
        return jsonify({
            "code": 400,
            "message": "Invalid JSON input: " + str(request.get_data())
        }), 400


#RECOMMEND
@app.route("/recommend", methods=['GET'])
def recommend_order():
    # Simple check of input format and data of the request are JSON
            try:
                data=[]
                result = processBatch(data, request.method, purchase_activity_URL)
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



def processBatch(data, method, ms):
    # Send the batch info to inventory
    # Invoke the inventory MS
    print('\n-----Invoking inventory microservice-----')
    URL = ms
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

