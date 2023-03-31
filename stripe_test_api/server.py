#! /usr/bin/env python3.6
"""
Python 3.6 or newer required.
"""
from flask import Flask, render_template, jsonify, request
import json
import os
import stripe

# This is your test secret API key.


app = Flask(__name__, static_folder='./client',
            static_url_path='', template_folder="./client")


stripe.api_key = 'sk_test_51MrG9JGDNnuttEbBYIMcbHJJTJFVZFp9TtignJgocaSNBN3f6tUxW6GJXIg4Ee8OpIHwkbbij8AWl0TotP4QsPLC00AWrQCmtL'


@app.route('/', methods=['GET'])
def create_payment():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242)
