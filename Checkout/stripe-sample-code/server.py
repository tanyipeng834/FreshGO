#! /usr/bin/env python3.6
"""
Python 3.6 or newer required.
"""
import json
import os
import stripe

# This is your test secret API key.
stripe.api_key = 'sk_test_51MoRioF9BRuNTM1y2Zqu5ciSOIM5xu9urXlclAmUn7YrsKKTV25D39Da1R3RBAEWjOwy9PbTfpiTGYwYTSiwNPIi00o45bpxKH'

from flask import Flask, render_template, jsonify, request


app = Flask(__name__, static_folder='public',
            static_url_path='', template_folder='public')


@app.route('/make_payment', methods=['POST'])
def create_payment():
    try:
        
        # data = json.loads(request.data)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=int(request.json.get('transaction_amt')*100),
            currency='sgd',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return jsonify({"status":'success'}),200
        
    except Exception as e:
        return jsonify(error=str(e)), 403
if __name__ == '__main__':
    app.run(port=5004)