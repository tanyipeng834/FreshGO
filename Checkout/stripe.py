from flask import Flask, request, jsonify, render_template
import os
import stripe
import json

app = Flask(__name__)

# Set your Stripe API secret key
stripe.api_key = 'sk_test_51MnzlnGVhDS4CcvmqQjbpgUhbOM5qlpbPAsw4onEl4fAhLWJlRsKlAhupYgvkAYgT1w8rYz0aApjZfkrxaClGS4H00wN4Oj5hW'

YOUR_DOMAIN = 'http://localhost:5004'

@app.route('/make_payment', methods=['POST'])
def create_payment():
    try:
        data = json.loads(request.data)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='sgd',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403
if __name__ == '__main__':
    app.run(port=4242)


# # Define a route to handle incoming purchase data from the "purchase_activity" microservice
# @app.route('/checkout_session', methods=['POST'])
# def create_checkout_session():
#     # Retrieve the product name and price from the JSON payload
#     # product_name = request.json['productName']
#     product_price = float(request.get['transaction_amt'])

#     # Create a new Stripe Checkout session with the specified product name and price
#     session = stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items=[{
#             'name': "FreshGo Payment",
#             'amount': product_price,
#             'currency': 'SGD',
#             'quantity': 1
#         }],
#         mode='payment',
#         success_url=YOUR_DOMAIN + '/success.html',
#         cancel_url=YOUR_DOMAIN + '/cancel.html',
#     )

#     # Return the session ID to the "purchase_activity" microservice
#     return True

# # Define a route to handle Stripe webhook events
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     # Retrieve the webhook event data from the request body
#     event = request.json
#     # Retrieve the Stripe webhook signature from the request headers
#     signature = request.headers.get('Stripe-Signature')

#     try:
#         # Verify the Stripe webhook event using your endpoint secret
#         webhook_event = stripe.Webhook.construct_event(event, signature, 'whsec_97H5L5UmTSBT8zBRDeUTBaxlohIu8Txs')

#         # Handle the "checkout.session.completed" event
#         if webhook_event['type'] == 'checkout.session.completed':
#             session = webhook_event['data']['object']
#             # Do any necessary post-payment processing here

#         return jsonify({'status': 'success'})

#     except stripe.error.SignatureVerificationError:
#         # Invalid signature
#         return jsonify({'status': 'signature_verification_error'}), 400

#     except Exception as e:
#         print(e)
#         return jsonify({'status': 'error'}), 400

# # Start the server

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
