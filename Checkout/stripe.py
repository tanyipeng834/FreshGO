from flask import Flask, request, jsonify
import os
import stripe

app = Flask(__name__)

# Set your Stripe API secret key
stripe.api_key = 'sk_test_51MnzlnGVhDS4CcvmqQjbpgUhbOM5qlpbPAsw4onEl4fAhLWJlRsKlAhupYgvkAYgT1w8rYz0aApjZfkrxaClGS4H00wN4Oj5hW'

YOUR_DOMAIN = 'http://localhost:5004'
# Define a route to handle incoming purchase data from the "purchase_activity" microservice
@app.route('/checkout_session', methods=['POST'])
def create_checkout_session():
    # Retrieve the product name and price from the JSON payload
    product_name = request.json['productName']
    product_price = request.json['productPrice']

    # Create a new Stripe Checkout session with the specified product name and price
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'name': product_name,
            'amount': product_price,
            'currency': 'SGD',
            'quantity': 1
        }],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success.html',
        cancel_url=YOUR_DOMAIN + '/cancel.html',
    )

    # Return the session ID to the "purchase_activity" microservice
    return jsonify({'sessionId': session.id})

# Define a route to handle Stripe webhook events
@app.route('/webhook', methods=['POST'])
def webhook():
    # Retrieve the webhook event data from the request body
    event = request.json
    # Retrieve the Stripe webhook signature from the request headers
    signature = request.headers.get('Stripe-Signature')

    try:
        # Verify the Stripe webhook event using your endpoint secret
        webhook_event = stripe.Webhook.construct_event(event, signature, 'whsec_97H5L5UmTSBT8zBRDeUTBaxlohIu8Txs')

        # Handle the "checkout.session.completed" event
        if webhook_event['type'] == 'checkout.session.completed':
            session = webhook_event['data']['object']
            # Do any necessary post-payment processing here

        return jsonify({'status': 'success'})

    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return jsonify({'status': 'signature_verification_error'}), 400

    except Exception as e:
        print(e)
        return jsonify({'status': 'error'}), 400

# Start the server

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
