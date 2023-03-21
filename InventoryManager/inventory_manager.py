from invokes import invoke_http
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os, sys
from os import environ
import json


app = Flask(__name__)
CORS(app)


# This will be the code for the farmer
inventory_URL = environ.get('order_URL') or "http://localhost:5000/inventory"

@app.route("/harvested/crops/<string:name>")
def place_order(name):
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            batch = request.get_json()
            print("\nReceived an batch order in JSON:", batch)

            # do the actual work
            # 1. Send harvested batch
            result = processBatch(batch)
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

def processBatch(batch):
    # Send the batch info to inventory
    # Invoke the inventory MS
    print('\n-----Invoking inventory microservice-----')
    order_result = invoke_http(inventory_URL, method='POST', json=batch)
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
    app.run(host='0.0.0.0', port=5000, debug=True)
