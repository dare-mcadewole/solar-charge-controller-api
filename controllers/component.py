from flask_json import as_json
from flask import request
from utils.http_errors import InvalidMethod

class ComponentController:
    @staticmethod
    @as_json
    def handle_component ():
        if request.method == 'GET':
            print("Request method: ", request.args)
            return {
                'name': 'GET /controller'
            }
        elif request.method == 'POST':
            return {
                'name': 'POST /controller'
            }
        return InvalidMethod
