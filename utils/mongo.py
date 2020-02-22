from app import app
from flask_pymongo import PyMongo

class MongoDB:
    _handle = None

    @staticmethod
    def get_db ():
        if not MongoDB._handle:
            MongoDB._handle = PyMongo(app)
        return MongoDB._handle

