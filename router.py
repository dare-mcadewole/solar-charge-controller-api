from controllers.component import ComponentController
from controllers.power import PowerController

class Router:
    @staticmethod
    def initialize (app):
        # API rule for /api/component
        app.add_url_rule(
            '/api/components',
            'component',
            ComponentController.handle_component,
            methods=[ 'GET', 'PUT', 'PATCH' ]
        )

        # API rule for /api/power
        app.add_url_rule(
            '/api/power',
            'power',
            PowerController.handle_power,
            methods=[ 'GET', 'POST' ]
        )
