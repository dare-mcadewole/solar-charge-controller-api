from pymongo import MongoClient
import os

class MongoDB:
    _handle = None

    @staticmethod
    def get_db ():
        if not MongoDB._handle:
            MongoDB._handle = MongoClient(os.getenv('MONGO_URI')).solar_charge_controller
        return MongoDB._handle

