import os
import logging
from flask import Flask
from logging.config import dictConfig

class Config(object):

    #: Database connection
    DB_API = os.getenv("DB_API", "")
    DB_USER = os.getenv("DB_USER", "")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_HOST = os.getenv("DB_HOST", "")
    DB_NAME = os.getenv("DB_NAME", "")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"{DB_API}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

    BUNDLE_ERRORS = True

app = Flask(__name__)
app.config.from_object(Config)
