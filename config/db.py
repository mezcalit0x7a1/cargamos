from .flask import app
from flask_sqlalchemy import SQLAlchemy

with app.app_context():
    db = SQLAlchemy(app, session_options={"autoflush": False})
