from flask import request
from flask_json import as_json
from utils.http_errors import InvalidMethod
from models.Power import Power 
from utils.pusher_client import PusherClient

class PowerController:
    @staticmethod
    @as_json
    def get_power ():
        return Power.get_by_date()

    @staticmethod
    @as_json
    def add ():
        value = request.get_json() if request.method == 'POST' else request.args
        value = value.get('value') if value else None
        if value:
            value = int(value) if str(value).isdigit() else value
            Power.save(value)
            PusherClient.trigger_power_update({
                'power': value
            })
            return {
                'power': value
            }
        return {
            'desc': 'Value not found',
            'status': 404
        }
