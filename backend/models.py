from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Kit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kit_number = db.Column(db.Integer, nullable=False, unique=True)
    location = db.Column(db.String(20), nullable=False)  # e.g., 'Row 1, Col 2', 'Pallet 41'
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    work_order = db.Column(db.String(50))
    techs = db.Column(db.String(100))  # Comma-separated tech names/IDs
    due_date = db.Column(db.String(20))
    parts = db.Column(db.Text)
    notes = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'kit_number': self.kit_number,
            'location': self.location,
            'status_id': self.status_id,
            'work_order': self.work_order,
            'techs': self.techs,
            'due_date': self.due_date,
            'parts': self.parts,
            'notes': self.notes
        }

    @staticmethod
    def from_dict(data):
        return Kit(
            kit_number=data.get('kit_number'),
            location=data.get('location'),
            status_id=data.get('status_id'),
            work_order=data.get('work_order'),
            techs=data.get('techs'),
            due_date=data.get('due_date'),
            parts=data.get('parts'),
            notes=data.get('notes')
        )

    def update_from_dict(self, data):
        for field in ['kit_number', 'location', 'status_id', 'work_order', 'techs', 'due_date', 'parts', 'notes']:
            if field in data:
                setattr(self, field, data[field])

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    color = db.Column(db.String(10))  # e.g., 'green', 'red', etc.
    kits = db.relationship('Kit', backref='status', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color
        }

class Tech(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
