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
    def get_components ():
        # GET request
        return Component.get()

    @staticmethod
    @as_json
    def update_components ():
        # PUT/PATCH request
        return {
            'PUT/PATCH': request.get_json(),
            'GET': request.args
        }
        componentValues = request.get_json() if request.method in [
            'PUT', 'PATCH'
        ] else request.query()
        if componentValues:
            components = {
                component: int(componentValues.get(component))
                if componentValues.get(component).isdigit()
                else componentValues.get(component)
                for component in componentValues.keys()
                if component in COMPONENTS
            }
            Component.save(components)
            PusherClient.trigger_components_update(components)
            return components
        return {
            'desc': 'Value not found',
            'status': 404
        }

    @staticmethod
    @as_json
    def get_component (component):
        if component in COMPONENTS:
            return Component.find(component)   
        return {
            'desc': 'Component not found',
            'status': 404
        }

    @staticmethod
    @as_json
    def update_component (component):
        if component in COMPONENTS:
            value = request.get_json() if request.method in [
                'PUT', 'PATCH'
            ] else request.args
            value = value.get('value') if value else None
            if value:
                value = int(value) if str(value).isdigit() else value
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
