from flask_json import as_json

class ComponentController:
    @staticmethod
    @as_json
    def get_controller ():
        return {
            "name": "Component controller"
        }
