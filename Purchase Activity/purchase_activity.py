#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script


from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector as sql

app = Flask(__name__)
CORS(app)



@app.route("/purchase_request", methods=['POST'])
def receiveLog():
    # Check if the request contains valid JSON
    log = None
    if request.is_json:
        log = request.get_json()
        processLog(log)
        # reply to the HTTP request
        return jsonify({"code": 200, "data": 'OK. Activity log printed.'}), 200 # return message; can be customized
    else:
        log = request.get_data()
        print("Received an invalid log:")
        print(log)
        print()
        return jsonify({"code": 400, "message": "Activity log input should be in JSON."}), 400 # Bad Request

def processLog(purchase_request):
    conn=sql.connect(host='localhost',user='root', password='',database='PURCHASE_ACTIVITY')
    print("Recording a log:")
    cursor= conn.cursor()
    sql="INSERT INTO purchase_activity (customer_id, crop_purchase, delivery_staff_id, customer_location, transaction_amount) VALUES (%s, %s)"
    customer_id=0
    crop_purchase=[]
    delivery_staff_id=0
    customer_location=''
    transaction_amount=0
    val=(customer_id, crop_purchase, delivery_staff_id, customer_location, transaction_amount)
    cursor.execute(sql, val)
    conn.commit()
    print() # print a new line feed as a separator
    print(cursor.rowcount,'record inserted')


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("This is flask for " + os.path.basename(__file__) + ": recording logs ...")
    app.run(host='0.0.0.0', port=5003, debug=True)
