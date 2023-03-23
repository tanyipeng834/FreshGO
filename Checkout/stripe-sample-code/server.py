#! /usr/bin/env python3.6
<<<<<<< HEAD
"""
Python 3.6 or newer required.
"""
=======
# """
# Python 3.6 or newer required.
# """
from flask import Flask, render_template, jsonify, request, redirect
>>>>>>> 8bde95b195e1dfdb48172dfae3759268aaae7517
import json
import os
import stripe
import requests
import webbrowser

# This is your test secret API key.
stripe.api_key = 'sk_test_51MoRioF9BRuNTM1y2Zqu5ciSOIM5xu9urXlclAmUn7YrsKKTV25D39Da1R3RBAEWjOwy9PbTfpiTGYwYTSiwNPIi00o45bpxKH'

<<<<<<< HEAD
from flask import Flask, render_template, jsonify, request

=======
>>>>>>> 8bde95b195e1dfdb48172dfae3759268aaae7517

app = Flask(__name__, static_folder='public',
            static_url_path='', template_folder='public')


@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:

        # data = json.loads(request.data)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=1000,
            currency='sgd',
<<<<<<< HEAD
=======
            # indicate that the payment should be made with a credit card
            # payment_method_types=['card'],
>>>>>>> 8bde95b195e1dfdb48172dfae3759268aaae7517
            automatic_payment_methods={
                'enabled': True,
            },
        )
<<<<<<< HEAD
        webbrowser.open_new_tab('http://localhost:4243/checkout.html')
        return jsonify({
            'clientSecret': intent['client_secret'],
            'Payment Status':"Success"
        })
        # return jsonify({"Payment Status":'Success'}),200
        
    except Exception as e:
        return jsonify(error=str(e)), 403
=======
        # return jsonify({"status":'success'}),200

        return jsonify({"Payment Status": 'Success'}), 200

        # Redirect the user to Stripe's hosted payment page using the url property of the first charge associated with the PaymentIntent.
        # return redirect(intent.charges.data[0].payment_method.url)

    except Exception as e:
        return jsonify(error=str(e)), 403


# @app.route('/payment_success', methods=['GET'])
# def payment_success():
#     return jsonify({"Payment Status":'Success'}),200


>>>>>>> 8bde95b195e1dfdb48172dfae3759268aaae7517
if __name__ == '__main__':
    app.run(port=4242)