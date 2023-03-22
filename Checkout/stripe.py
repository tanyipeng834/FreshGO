import stripe
from flask import Flask, jsonify, request

app = Flask(__name__)

# Set the Stripe API key
stripe.api_key = "sk_test_51MnzlnGVhDS4CcvmqQjbpgUhbOM5qlpbPAsw4onEl4fAhLWJlRsKlAhupYgvkAYgT1w8rYz0aApjZfkrxaClGS4H00wN4Oj5hW"

@app.route('/process_payment', methods=['POST'])
def process_payment():
    # Get the total price from the request body
    total_price = request.json['total_price']

    # Create a Stripe payment intent
    intent = stripe.PaymentIntent.create(
        amount=total_price,
        currency='SGD'
    )

    return jsonify({"client_secret": intent.client_secret})

@app.route('/payment_complete', methods=['POST'])
def payment_complete():
    # Get the payment intent ID from the request body
    intent_id = request.json['intent_id']

    # Retrieve the payment intent from Stripe
    intent = stripe.PaymentIntent.retrieve(intent_id)

    # Check if the payment was successful
    if intent.status == 'succeeded':
        # Create a request in the Purchase Activity microservice with the product list and the total price
        request.post('http://purchase_activity/create_request', json={
            "total_price": intent.amount
        })

    return jsonify({"message": "Payment complete!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
