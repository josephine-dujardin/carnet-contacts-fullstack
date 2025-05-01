# === BACKEND (Flask) ===
# app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autorise les appels depuis React en local

# Données fictives pour l'exemple
contacts = [
    {"id": 1, "name": "Alice Martin", "email": "alice@example.com", "phone": "0601020304"},
    {"id": 2, "name": "Bob Dupont", "email": "bob@example.com", "phone": "0605060708"},
    {"id": 3, "name": "Chloé Dubois", "email": "chloe@example.com", "phone": "0609091011"}
]

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

if __name__ == '__main__':
    app.run(debug=True)