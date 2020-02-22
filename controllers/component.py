from flask_json import as_json
from flask import request
from utils.http_errors import InvalidMethod
from utils.mongo import MongoDB
from models.Component import Component 

ALLOWED_COMPONENTS = [
    'solar_irradiance',
    'exporting',
    'current_usage',
    'temperature',
    'humidity',
    'depth_of_discharge',
    'load',
    'battery_status',
    'module_id'
]

class ComponentController:
    @staticmethod
    @as_json
    def handle_component (component):
        if component in ALLOWED_COMPONENTS:
            # GET request
            if request.method == 'GET':
                return Component.get(component)

            # PUT/PATCH request
            elif request.method in [ 'PUT', 'PATCH' ]:
                value = request.get_json().get('value')
                if value:
                    return Component.save(component, value)
                    # return {
                    #     'component': component,
                    #     'value': value
                    # }
                else:
                    return {
                        'description': 'Value not found',
                        'status': 404
                    }
            return InvalidMethod
        return {
            'description': 'Component \'%s\' not found' % component,
            'status': 404
        }
