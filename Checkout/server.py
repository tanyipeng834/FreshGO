#! /usr/bin/env python3.6
# """
# Python 3.6 or newer required.
# """
from flask import Flask, render_template, jsonify, request, redirect
import json
import os
import stripe
import requests
import webbrowser

# This is your test secret API key.
stripe.api_key = 'sk_test_51MoRioF9BRuNTM1y2Zqu5ciSOIM5xu9urXlclAmUn7YrsKKTV25D39Da1R3RBAEWjOwy9PbTfpiTGYwYTSiwNPIi00o45bpxKH'


app = Flask(__name__, static_folder='public',
            static_url_path='', template_folder='public')


@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:

        #data = json.loads(request.data)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=2.40,
            currency='sgd',
            # indicate that the payment should be made with a credit card
            # payment_method_types=['card'],
            automatic_payment_methods={
                'enabled': True,
            },
        )
        webbrowser.open_new_tab('http://stripeapi:4243/checkout.html')
        return jsonify({
            'clientSecret': intent['client_secret'],
            'Payment Status': "Success"
        })
        # return jsonify({"Payment Status":'Success'}),200

    except Exception as e:
        return jsonify(error=str(e)), 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242)
