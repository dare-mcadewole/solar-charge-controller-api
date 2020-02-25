from flask_json import as_json
from flask import request
from utils.http_errors import InvalidMethod
from models.Component import Component 
from utils.pusher_client import PusherClient

COMPONENTS = [
    'si', # Solar Irradiance
    'e', # Exporting
    'cu', # Current Usage
    't', # Temperature
    'h', # Humidity
    'dod', # Depth of discharge
    'l', # Load
    'bs', # Battery Status
    'mi' # Module ID
]

class ComponentController:
    @staticmethod
    @as_json
    def handle_components ():
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
                    for component in COMPONENTS
                    if component in componentValues
                }
                Component.save(components)
                PusherClient.trigger_components_update(components)
                return components
            return {
                'desc': 'Value not found',
                'status': 404
            }
        return InvalidMethod

    @staticmethod
    @as_json
    def handle_component (component):
        if component in COMPONENTS:
            if request.method == 'GET':
                return Component.find(component)

            else:
                value = request.get_json().get('value')
                if value:
                    value = int(value) if value.isdigit() else value
                    Component.set(component, value)
                    PusherClient.trigger_component_update({
                        'component': component,
                        'value': value
                    })
                    return {
                        'component': component,
                        'value': value
                    }
                return {
                    'desc': 'Value not found',
                    'status': 404
                }
                
        return {
            'desc': 'Component not found',
            'status': 404
        }
