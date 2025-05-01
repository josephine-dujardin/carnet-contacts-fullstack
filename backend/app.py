from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:monpassword@localhost/carnet_contacts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# === Contact ===
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email, "phone": self.phone}

# === Routes ===
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([c.to_dict() for c in contacts])

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.json
    contact = Contact(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(contact)
    db.session.commit()
    return jsonify(contact.to_dict()), 201

@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({"message": "Contact non trouvé"}), 404
    data = request.json
    contact.name = data['name']
    contact.email = data['email']
    contact.phone = data['phone']
    db.session.commit()
    return jsonify(contact.to_dict())

@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({"message": "Contact non trouvé"}), 404
    db.session.delete(contact)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
