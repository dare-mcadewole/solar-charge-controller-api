from flask_json import as_json, JsonError
from flask import request

InvalidMethod = JsonError(
    description = 'Invalid HTTP method',
    code = 405
)

class ComponentController:
    @staticmethod
    @as_json
    def get_component ():
        if request.method == 'GET':
            print("Request method: ", request.args)
            return {
                'name': 'Component-Controller'
            }
        return InvalidMethod

    @staticmethod
    @as_json
    def post_component ():
        if request.method == 'POST':
            return {
                'route': 'POST /component'
            }
        return InvalidMethod
