from flask import Flask, render_template, jsonify, request, redirect
from flask_cors import CORS
import stripe
import requests
import webbrowser


app = Flask(__name__)
CORS(app)
api_key = 'sk_test_51MrG9JGDNnuttEbBYIMcbHJJTJFVZFp9TtignJgocaSNBN3f6tUxW6GJXIg4Ee8OpIHwkbbij8AWl0TotP4QsPLC00AWrQCmtL'


@app.route('/payment', methods=['POST'])
if __name__ == '__main__':
    app.run(port=4243)
