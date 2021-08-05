# -*- coding: utf-8 -*-
"""
    config.db
    ~~~~~~~~~~~~~~
    Instance DB connection
    :copyright: (c) 2021 by Luis Rdz
"""
from .flask import app
from flask_sqlalchemy import SQLAlchemy

with app.app_context():
    db = SQLAlchemy(app, session_options={"autoflush": False})
