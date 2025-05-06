from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='backend/static')
CORS(app)

@app.route('/backend/')
def hello():
    return jsonify({'message': 'Ciao dal backend!'})

# Serve React static build
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        # Se la risorsa non esiste, restituiamo index.html (SPA)
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()