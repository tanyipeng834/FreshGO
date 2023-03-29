from invokes import invoke_http
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import sys
from os import environ
import json

# /manager method=GET retrieves all crops and quantity and their status
# /manager method=POST inserts crop into table: name must be unique
        # {
        # "name": "Xin Gua",
        # "quantity": 30
        # }
# /manager method=PUT updates crop value, farmer puts how many crops they wanna add to inventory
        # {
        # "name": "Xin Gua",
        # "quantity": 30
        # }
# /recommend method=GET without json, retreieves all purchase_activity
# /recommend method=GET with json, retreieves all purchase_activity for past month
#                                  that is the same crop_name, quantity = current inventory
        # {
        # "name": "Xin Gua",
        # "quantity": 20
        # }
        # information will be retrieved from UI from table created with /manager method=GET

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
@app.route("/manager/<string:name>", methods=['GET'])
def recommend(name):
    # Simple check of input format and data of the request are JSON
    inventory_response = invoke_http(f'http://localhost:5000/inventory/{name}')
    current_inventory = inventory_response['data']['data']['quantity']
    purchase_activity = invoke_http(f'http://localhost:5006/purchase_request/{name}')
    puchase


    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)

