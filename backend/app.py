from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

contacts = [
    {"id": 1, "name": "Alice Martin", "email": "alice@example.com", "phone": "0601020304"},
    {"id": 2, "name": "Bob Dupont", "email": "bob@example.com", "phone": "0605060708"},
    {"id": 3, "name": "Chloé Dubois", "email": "chloe@example.com", "phone": "0609091011"}
]

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.json
    new_id = max(contact["id"] for contact in contacts) + 1 if contacts else 1
    new_contact = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"],
        "phone": data["phone"]
    }
    contacts.append(new_contact)
    return jsonify(new_contact), 201

@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    data = request.json
    for contact in contacts:
        if contact['id'] == id:
            contact['name'] = data['name']
            contact['email'] = data['email']
            contact['phone'] = data['phone']
            return jsonify(contact)
    return jsonify({"message": "Contact non trouvé"}), 404

@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    global contacts
    contacts = [contact for contact in contacts if contact['id'] != id]
    return '', 204  # No content, suppression réussie

if __name__ == '__main__':
    app.run(debug=True)
