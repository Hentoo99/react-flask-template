# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/hello")
def hello():
    return jsonify(message="Ciao dal backend!")

if __name__ == "__main__":
    app.run(debug=True)