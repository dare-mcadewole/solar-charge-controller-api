from flask import request
from flask_json import as_json
from utils.http_errors import InvalidMethod

class PowerController:
    @staticmethod
    @as_json
    def handle_power ():
        if request.method == 'GET':
            return {
                'name': 'GET /power'
            }
        elif request.method == 'POST':
            return {
                'name': 'POST /power'
            }
        return InvalidMethod
