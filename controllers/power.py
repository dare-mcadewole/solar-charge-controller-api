from flask import request
from flask_json import as_json
from utils.http_errors import InvalidMethod
from models.Power import Power 
from utils.pusher_client import PusherClient

class PowerController:
    @staticmethod
    @as_json
    def handle_power ():
        if request.method == 'GET':
            return Power.get_by_date()
        elif request.method == 'POST':
            value = request.get_json().get('value')
            if value:
                Power.save(value)
                PusherClient.trigger_power_update({
                    'power': value
                })
                return {
                    'power': value
                }
            return {
                'description': 'Value not found',
                'status': 404
            }
        return InvalidMethod
