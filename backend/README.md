# Backend for Kitting Visualization Prototype

Flask REST API for managing kits, statuses, and technicians.

Directory structure:
- backend/
    - app.py
    - models.py
    - db.sqlite3 (created at runtime)

---

## app.py
- Main Flask app
- API endpoints for kits, statuses, and techs

## models.py
- SQLAlchemy models for Kits, Statuses, Techs

---

## To run:
1. Install dependencies: `pip install flask flask-cors sqlalchemy`
2. Run: `python app.py`

---

## Note
- This is a prototype using SQLite. For production, migrate to Oracle.
