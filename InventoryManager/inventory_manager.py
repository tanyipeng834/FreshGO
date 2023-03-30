from invokes import invoke_http
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from os import environ


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

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'inventory_manager_URL') or "mysql+mysqlconnector://root@localhost:3306/inventory_manager"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# docker run --name inventory_manager --network my-net -e inventory_manager_URL=mysql+mysqlconnector://is213@host.docker.internal:3306/inventory_manager mosengtim2021/inventory_manager:1.0

# This will be the code for the farmer
inventory_URL = environ.get("inventory_URL") or "http://localhost:5000/inventory"
purchase_activity_URL = "http://localhost:5006/purchase_request"


db = SQLAlchemy(app)

# CRUD Inventory


@app.route("/manager/<string:name>", methods=['GET'])
def recommend(name):
    
    try:
        # Simple check of input format and data of the request are JSON
        inventory_response = invoke_http(
            f'http://localhost:5000/inventory/{name}')

        current_inventory = inventory_response['data']['quantity']

        purchase_response = invoke_http(
            f'http://localhost:5006/purchase_request/{name}')

        purchase_activity = purchase_response["Total Sales"]

        # Get the
        crop_management_response = invoke_http(
            f'http://localhost:5001/crop_management/{name}')
        ongrowing_crops = crop_management_response["data"]
        number_of_on_growing_crops = len(ongrowing_crops)
        total_crops_grown = purchase_activity - \
            number_of_on_growing_crops-current_inventory
        if (total_crops_grown < 0):
            total_crops_grown = 0

    except:
        return jsonify(
            {
                "code": 404,
                "message": "There is an error accessing the Inventory Manager microservice."
            }
        ), 404

    return jsonify(
        {
            "code": 200,
            "ongrowingCrops": number_of_on_growing_crops,
            "inventory": current_inventory,
            "purchaseActivity": purchase_activity,
            "totalCrop": total_crops_grown
        }
    ), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
