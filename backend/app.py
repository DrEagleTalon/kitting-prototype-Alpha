from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Kit, Status, Tech

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()

# Kits endpoints
@app.route('/api/kits', methods=['GET'])
def get_kits():
    kits = Kit.query.all()
    return jsonify([kit.to_dict() for kit in kits])

@app.route('/api/kits', methods=['POST'])
def add_kit():
    data = request.json
    kit = Kit.from_dict(data)
    db.session.add(kit)
    db.session.commit()
    return jsonify(kit.to_dict()), 201

@app.route('/api/kits/<int:kit_id>', methods=['GET'])
def get_kit(kit_id):
    kit = Kit.query.get_or_404(kit_id)
    return jsonify(kit.to_dict())

@app.route('/api/kits/<int:kit_id>', methods=['PUT'])
def update_kit(kit_id):
    kit = Kit.query.get_or_404(kit_id)
    data = request.json
    kit.update_from_dict(data)
    db.session.commit()
    return jsonify(kit.to_dict())

@app.route('/api/kits/<int:kit_id>', methods=['DELETE'])
def delete_kit(kit_id):
    kit = Kit.query.get_or_404(kit_id)
    db.session.delete(kit)
    db.session.commit()
    return '', 204

# Statuses endpoint
@app.route('/api/statuses', methods=['GET'])
def get_statuses():
    statuses = Status.query.all()
    return jsonify([status.to_dict() for status in statuses])

# Techs endpoint
@app.route('/api/techs', methods=['GET'])
def get_techs():
    techs = Tech.query.all()
    return jsonify([tech.to_dict() for tech in techs])

if __name__ == '__main__':
    app.run(debug=True)
