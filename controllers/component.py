from flask_json import as_json
from flask import request
from utils.http_errors import InvalidMethod
from models.Component import Component 
from utils.pusher_client import PusherClient

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
    def handle_component ():
        # GET request
        if request.method == 'GET':
            return Component.get()

        # PUT/PATCH request
        elif request.method in [ 'PUT', 'PATCH' ]:
            componentValues = request.get_json()
            if componentValues:
                components = {
                    component: int(componentValues.get(component))
                    if componentValues.get(component).isdigit()
                    else componentValues.get(component)
                    for component in ALLOWED_COMPONENTS
                }
                Component.save(components)
                PusherClient.trigger_component_update(components)
                return components
            return {
                'description': 'Value not found',
                'status': 404
            }
        return InvalidMethod
